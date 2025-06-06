# Reconhecimento-Facial-IA
Este projeto utiliza Python e as bibliotecas OpenCV e face-recognition para identificar pessoas conhecidas através de uma webcam em tempo real. O sistema carrega um banco de dados de imagens de uma pasta local, aprende as características faciais de cada pessoa e, em seguida, as reconhece no vídeo ao vivo.

Demonstração
Dica: Grave um GIF do seu programa funcionando e substitua o placeholder abaixo! Ferramentas como ScreenToGif (Windows) ou Kap (macOS) são ótimas para isso.

Funcionalidades
Reconhecimento em Tempo Real: Identifica faces diretamente do feed da webcam.
Banco de Dados Dinâmico: Basta adicionar ou remover arquivos de imagem de uma pasta para atualizar a lista de pessoas conhecidas.
Feedback Visual: Desenha um retângulo e exibe o nome da pessoa identificada na tela.
Otimização de Performance: Processa frames de forma alternada para garantir uma experiência mais fluida e com maior FPS.
Identificação de Desconhecidos: Rotula como "Desconhecido" qualquer rosto que não corresponda a ninguém no banco de dados.
Tecnologias Utilizadas
Python 3.9+
OpenCV (opencv-python): Para captura e manipulação de vídeo.
face-recognition: Biblioteca principal para localizar e comparar faces (baseada na dlib).
dlib: Toolkit de machine learning em C++ que faz o trabalho pesado.
NumPy: Para manipulação eficiente de arrays de imagem.

1. Pré-requisitos (Essencial para Windows)
A biblioteca dlib precisa ser compilada durante a instalação, o que exige um ambiente de desenvolvimento C++ e a ferramenta CMake.

Ferramentas de Compilação C++: Instale o "Build Tools for Visual Studio" a partir do site oficial da Microsoft. Durante a instalação, selecione a carga de trabalho "Desenvolvimento para desktop com C++".
CMake: Baixe e instale o CMake a partir do site oficial. É crucial que, durante a instalação, você marque a opção para Adicionar o CMake ao PATH do sistema.
