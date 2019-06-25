# MLP GAN
## Environment：
Windows 10

Python 3.5

matplotlib             2.2.3

music21                5.7.0

Keras                  2.2.4

tensorflow-gpu         1.5.0

wxPython               4.0.6

pygame                 1.9.6



## Data：
data:古筝数据集 musics of guzheng

data_erhu:二胡数据集 musics of erhu

note_g: notes list for guzheng  训练好的古筝音符表

note_e: notes list for erhu     训练好的二胡音符表 

## Usage

Must train first，because the models I saved are too large to be uploaded.

GAN_G.py:training for the guzheng music

GAN_E.PY:training for the erhu music

ui.py: the ui for generate,tap ‘生成’ to generate the music,and '播放' to play the music

