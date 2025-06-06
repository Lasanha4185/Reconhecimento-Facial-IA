import face_recognition as fr
import cv2
import numpy as np
import os


# --- PASSO 1: CARREGAR AS FACES CONHECIDAS (O MESMO DE ANTES) ---

def carregar_encodings_conhecidos(pasta):
    """
    Lê todas as imagens de uma pasta, aprende o rosto de cada uma
    e retorna uma lista de encodings e seus respectivos nomes.
    """
    lista_encodings_conhecidos = []
    lista_nomes_conhecidos = []

    print("Carregando imagens conhecidas...")
    for nome_arquivo in os.listdir(pasta):
        caminho_completo = os.path.join(pasta, nome_arquivo)
        imagem = fr.load_image_file(caminho_completo)
        encodings = fr.face_encodings(imagem)

        if encodings:
            lista_encodings_conhecidos.append(encodings[0])
            nome_pessoa = os.path.splitext(nome_arquivo)[0]
            lista_nomes_conhecidos.append(nome_pessoa)
            print(f"  - Rosto de '{nome_pessoa.title()}' carregado.")
        else:
            print(f"  - AVISO: Nenhuma face encontrada em '{nome_arquivo}'.")

    return lista_encodings_conhecidos, lista_nomes_conhecidos


# Carrega as faces que o programa deve "conhecer"
encodings_conhecidos, nomes_conhecidos = carregar_encodings_conhecidos('imagens_conhecidas')
print("\nBase de dados de faces conhecidas carregada. Iniciando webcam...")

# --- PASSO 2: INICIAR A WEBCAM E PROCESSAR EM TEMPO REAL ---

# Inicializa a webcam. O '0' geralmente se refere à webcam padrão.
cap = cv2.VideoCapture(0)

# Variáveis para otimização
locations_faces_quadro = []
encodings_faces_quadro = []
nomes_faces_quadro = []
processar_este_quadro = True

while True:
    # Captura um único frame da webcam
    ret, frame = cap.read()
    if not ret:
        print("Erro: Não foi possível capturar imagem da webcam.")
        break

    # Otimização: processa apenas um a cada dois frames para economizar recursos
    if processar_este_quadro:
        # Reduz o tamanho do frame para processamento mais rápido (1/4 do original)
        frame_pequeno = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # Converte o frame de BGR (padrão OpenCV) para RGB (padrão face_recognition)
        frame_pequeno_rgb = cv2.cvtColor(frame_pequeno, cv2.COLOR_BGR2RGB)

        # Encontra todas as faces e encodings no frame atual
        locations_faces_quadro = fr.face_locations(frame_pequeno_rgb)
        encodings_faces_quadro = fr.face_encodings(frame_pequeno_rgb, locations_faces_quadro)

        nomes_faces_quadro = []
        for encoding_rosto in encodings_faces_quadro:
            comparacoes = fr.compare_faces(encodings_conhecidos, encoding_rosto)
            nome = "Desconhecido"

            # Usa a distância facial para encontrar a melhor correspondência
            distancias_faciais = fr.face_distance(encodings_conhecidos, encoding_rosto)
            melhor_match_index = np.argmin(distancias_faciais)

            if comparacoes[melhor_match_index]:
                nome = nomes_conhecidos[melhor_match_index]

            nomes_faces_quadro.append(nome)

    # Inverte o status para o próximo frame
    processar_este_quadro = not processar_este_quadro

    # --- PASSO 3: EXIBIR OS RESULTADOS (A CADA FRAME) ---

    # Itera sobre os resultados da ÚLTIMA detecção para exibir de forma fluida
    for (top, right, bottom, left), nome in zip(locations_faces_quadro, nomes_faces_quadro):
        # Como redimensionamos o frame para detectar, precisamos escalar as coordenadas de volta
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Desenha o retângulo ao redor do rosto
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Escreve o nome abaixo do rosto
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        fonte = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, nome.title(), (left + 6, bottom - 6), fonte, 1.0, (255, 255, 255), 1)

    # Mostra o resultado na tela
    cv2.imshow('Reconhecimento Facial em Tempo Real', frame)

    # Pressione 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- PASSO 4: FINALIZAR O PROGRAMA ---

# Libera o acesso à webcam e fecha todas as janelas
cap.release()
cv2.destroyAllWindows()
print("Webcam finalizada e janelas fechadas.")