# SynDataGeneration

Este código é usado para gerar cenas sintéticas para a tarefa de detecção de instância/objeto. Dadas imagens de objetos isolados de várias visualizações e algumas cenas de fundo, ele gera cenas completas com vários objetos e arquivos de anotações que podem ser usados ​​para treinar um detector de objetos. A abordagem usada para geração funciona bem com métodos de detecção de objetos baseados em região como [Faster R-CNN](https://github.com/rbgirshick/py-faster-rcnn).

## Pré-requisitos
1. OpenCV (pip install opencv-python)
2. PIL (almofada de instalação de pip)
3. Mistura Poisson (Siga as instruções [aqui](https://github.com/yskmt/pb)
4. PyBlur (pip instala pyblur)

Para poder gerar cenas, este código pressupõe que você tenha as máscaras de objeto para todas as imagens. Não há pré-requisito sobre qual algoritmo é usado para gerar essas máscaras, pois para diferentes aplicações, diferentes algoritmos podem acabar fazendo um bom trabalho. No entanto, recomendamos [Pixel Objectness with Bilinear Pooling](https://github.com/debidatta/pixelobjectness-bp) para gerar automaticamente essas máscaras. Se você quiser anotar a imagem manualmente, recomendamos os algoritmos GrabCut([aqui](https://github.com/opencv/opencv/blob/master/samples/python/grabcut.py), [aqui](https:// github.com/cmuartfab/grabcut), [aqui](https://github.com/daviddoria/GrabCut))

## Configurando padrões
A primeira seção do arquivo defaults.py contém caminhos para vários arquivos e bibliotecas. Configure-os de acordo.

Os outros padrões referem-se a diferentes parâmetros de geração de imagem que podem ser variados para produzir cenas com diferentes níveis de desordem, oclusão, aumento de dados etc.

## Executando o script
```
python dataset_generator.py [-h] [--selecionado] [--scale] [--rotation]
                            [--num NUM] [--dontocclude] [--add_distractors]
                            exp raiz

Criar conjunto de dados com diferentes ampliações

argumentos posicionais:
  root O diretório raiz que contém as imagens e
                     anotações.
  exp O diretório onde as imagens e listas de anotações serão
                     criada.

argumentos opcionais:
  -h, --help mostra esta mensagem de ajuda e sai
  --selected Mantém apenas instâncias selecionadas no conjunto de dados de teste. Predefinição
                     é manter todas as instâncias no diretório roo.
  --scale Adicionar aumento de escala. O padrão é não adicionar escala
                     aumento.
  --rotation Adicionar aumento de rotação. O padrão é não adicionar rotação
                     aumento.
  --num NUM Número de vezes que cada imagem estará no conjunto de dados
  --dontocclude Adiciona objetos sem oclusão. O padrão é produzir
                     oclusões
  --add_distractors Adiciona objetos distratores. O padrão é não usar
                     distrações
```

## Treinando um detector de objetos
O código produz todos os arquivos necessários para treinar um detector de objetos. O formato é diretamente útil para Faster R-CNN, mas também pode ser adaptado para diferentes detectores de objetos. Os diferentes arquivos produzidos são:
1. __labels.txt__ - Contém os rótulos dos objetos que estão sendo treinados
2. __annotations/*.xml__ - Contém arquivos de anotação em formato XML que contêm anotações de caixa delimitadora para várias cenas
3. __images/*.jpg__ - Contém arquivos de imagem das cenas sintéticas em formato JPEG
4. __train.txt__ - Contém uma lista de arquivos de imagem sintética e arquivos de anotação correspondentes

Existem tutoriais que descrevem como se pode adaptar o código Faster R-CNN para executar em um conjunto de dados personalizado como:
1. https://github.com/rbgirshick/py-faster-rcnn/issues/243
2. http://sgsai.blogspot.com/2016/02/training-faster-r-cnn-on-custom-dataset.html

## Papel

O código foi usado para gerar cenas sintéticas para o artigo [Cut, Paste and Learn: Surprisingly Easy Synthesis for Instance Detection](https://arxiv.org/abs/1708.01642).

Se você achar nosso código útil em sua pesquisa, considere citar:
```
@InProceedings{Dwibedi_2017_ICCV,
autor = {Dwibedi, Debidatta e Misra, Ishan e Hebert, Martial},
title = {Recortar, Colar e Aprender: Síntese Surpreendentemente Fácil para Detecção de Instâncias},
booktitle = {The IEEE International Conference on Computer Vision (ICCV)},
mês = {out},
ano = {2017}
}
```