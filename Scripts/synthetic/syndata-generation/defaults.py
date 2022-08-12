# coding=utf-8

BACKGROUND_DIR = 'demo_data_dir/backgrounds/'
BACKGROUND_GLOB_STRING = '*.jpg'
POISSON_BLENDING_DIR = '/content/Scripts-Dataset/Scripts/synthetic/syndata-generation/pb'
SELECTED_LIST_FILE = 'demo_data_dir/selected.txt'
DISTRACTOR_LIST_FILE = 'demo_data_dir/neg_list.txt'
DISTRACTOR_DIR = 'demo_data_dir/distractor_objects_dir/'
DISTRACTOR_GLOB_STRING = '*.jpg'
INVERTED_MASK = False # Defina como verdadeiro se os pixels brancos representarem o plano de fundo

# Parameters for generator
NUMBER_OF_WORKERS = 4
BLENDING_LIST = ['none']

# Parameters for images
MIN_NO_OF_OBJECTS = 1 # <<<<<<
MAX_NO_OF_OBJECTS = 3 # <<<<<<
MIN_NO_OF_DISTRACTOR_OBJECTS = 0
MAX_NO_OF_DISTRACTOR_OBJECTS = 0
WIDTH = 640
HEIGHT = 480
MAX_ATTEMPTS_TO_SYNTHESIZE = 20

# Parameters for objects in images
MIN_SCALE = 0.15 # min scale for scale augmentation ---mudar esses parametros caso a imagem nao fique satisfatoria # <<<<<<
MAX_SCALE = 0.20 # max scale for scale augmentation ----mudar esses parametros caso a imagem nao fique satisfatoria # <<<<<<
MAX_DEGREES = 90 # rotação máxima permitida durante o aumento de rotação # <<<<<<
MAX_TRUNCATION_FRACTION = 0.25 # fração máxima a ser truncada = MAX_TRUNCACTION_FRACTION*(WIDTH/HEIGHT)
MAX_ALLOWED_IOU = 0.1 # IOU > MAX_ALLOWED_IOU é considerado uma oclusão
MIN_WIDTH = 6 # Largura mínima do objeto a ser usado para geração de dados
MIN_HEIGHT = 6 # Altura mínima do objeto a ser usado para geração de dados