# Sistema de Gerenciamento de Requisições com Identificação de Clientes por Hash

## Descrição
Este sistema é uma aplicação Python projetada para gerenciar e processar requisições de clientes usando partes de hashes para identificação única. O sistema extrai e compara segmentos de hash para verificar a identidade de cada cliente, permitindo o tratamento personalizado das suas respectivas requisições.

## Características
- **Identificação Única de Clientes:** Utiliza uma parte do hash da requisição para identificar cada cliente de maneira única e segura.
- **Processamento Personalizado:** Permite o processamento diferenciado das requisições com base na identidade do cliente.

## Instalação
Para instalar e configurar o sistema, siga os passos abaixo:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
pip install -r requirements.txt
```

## Uso
Para usar o sistema, inicie o servidor com o seguinte comando:

```bash
python app/main.py
```

Envie requisições para o sistema usando sua ferramenta ou biblioteca preferida para simular requisições de cliente.

## Testes
Para executar os testes e verificar a integridade do sistema, utilize:

```bash
python -m unittest discover -s tests
```

## Contribuição
Contribuições para o projeto são bem-vindas. Para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b nova-feature`).
3. Faça commit das suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Envie para a branch (`git push origin nova-feature`).
5. Abra um Pull Request.

## Licença
Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

