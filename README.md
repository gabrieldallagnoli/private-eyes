# Private Eyes

## Problema

Minha estação de trabalho está posicionada de frente para a porta do quarto. Isso permite que qualquer pessoa que entre veja minha tela imediatamente, além de poder me surpreender sem que eu perceba sua aproximação.

## Solução

Implementei um sistema simples de detecção de movimento utilizando a câmera de um smartphone apontada para a porta. O celular transmite o vídeo via IP, e um script em Python com OpenCV processa os quadros em tempo real. Ao detectar movimento, o sistema envia um sinal ao meu computador, permitindo a execução de ações customizadas (como notificações, bloqueio de tela, etc).

## Tecnologias Utilizadas

- Smartphone com aplicativo **IP Webcam**
    
- Python com biblioteca **OpenCV**
    
- Conexão local (Wi-Fi)
    

## Resultado

Sempre que há movimentação na porta, sou imediatamente notificado no PC. O sistema é leve, eficiente e fácil de adaptar para outros comportamentos.
