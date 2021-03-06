## Testruns
Listing of test runs and results.


### COSY (Reduced Dataset)
| train_dir             | Server | BS | Input   | Norm.        | Units | Ep | Layout | Loss   | MED   | WER    | Notes          |
|-----------------------|--------|---:|---------|--------------|------:|---:|-------:|-------:|------:|-------:|----------------|
| `3d1r2d_global`       | cosy14 |  8 | 80 Mel  | global       |  2048 | 20 | 3d1r2d | 30.594 | 0.113 | 0.3195 |                |
| `3d1r2d_local`        | cosy15 |  8 | 80 Mel  | local        |  2048 | 20 | 3d1r2d | 29.022 | 0.107 | 0.3086 |                |
| `3d1r2d_local_scalar` | cosy16 |  8 | 80 Mel  | local scalar |  2048 | 20 | 3d1r2d | 31.882 | 0.114 | 0.3214 |                |
| `3d1r2d_none`         | cosy14 |  8 | 80 Mel  | none         |  2048 | 20 | 3d1r2d | 29.604 | 0.112 | 0.317  |                |
| `3d1r2d_mfcc_local`   | cosy15 |  8 | 80 MFCC | local        |  2048 | 20 | 3d1r2d | 24.633 | 0.088 | 0.255  |                |
| `3d1r2d_local_3000u`  | cosy16 |  8 | 80 Mel  | local        |  3000 | 20 | 3d1r2d | 34.556 | 0.102 | 0.290  |                |


#### Reduced Dataset
Note that runs marked with *Reduced Dataset* did not use the complete dataset.
* train: timit, tedlium, libri_speech, common_voice, ~~tatoeba~~
* test: libri_speech, common_voice
* dev: libri_speech


### COSY
| train_dir                      | Server | BS | Input   | Norm.        | Units | Ep | Layout | Loss   | MED   | WER    | Notes         |
|--------------------------------|--------|---:|---------|--------------|------:|---:|-------:|-------:|------:|-------:|---------------|
| `3d1r2d_global_mfcc_full`      | cosy14 |  8 | 80 MFCC | global       |  2048 | 20 | 3d1r2d | 25.606 | 0.106 | 0.304  |               |
| `3d2r2d_local_mfcc_full`       | cosy15 |  8 | 80 MFCC | local        |  2048 | 16 | 3d2r2d | 18.988 | 0.074 | 0.211  |               |
| `3d1r2d_global_mel_full`       | cosy14 |  8 | 80 Mel  | global       |  2048 | 14 | 3d1r2d | 31.399 | 0.131 | 0.371  |               |
| `3d1r2d_local_mel_full`        | cosy15 |  8 | 80 Mel  | local        |  2048 | 15 | 3d1r2d | 29.520 | 0.125 | 0.354  |               |
| `3d1r2d_local_scalar_mel_full` | cosy16 |  8 | 80 Mel  | local scalar |  2048 | 15 | 3d1r2d | 31.669 | 0.132 | 0.373  |               |
| `3d1r2d_none_mel_full`         | cosy17 |  8 | 80 Mel  | none         |  2048 | 16 | 3d1r2d | 32.006 | 0.135 | 0.376  |               |
| `3d1r2d_none_mfcc_full`        | cosy14 |  8 | 80 MFCC | none         |  2048 |  8 | 3d1r2d | 23.865 | 0.096 | 0.273  |               |
| `3d1r2d_none_mel_full_2`       | cosy14 |  8 | 80 Mel  | none         |  2048 |  8 | 3d1r2d | 28.915 | 0.121 | 0.335  | For R. above. |
| `3c1r2d_mel_local_full`        | cosy17 |  8 | 80 Mel  | local        |  2048 |  8 | 3c1r2d | 22.695 | 0.091 | 0.2557 |               |
| `3c1r2d_mel_localscalar_full`  | cosy14 |  8 | 80 Mel  | local scalar |  2048 |  9 | 3c1r2d | 23.579 | 0.090 | 0.2556 |               |
| `3c1r2d_mel_global_full`       | cosy15 |  8 | 80 Mel  | global       |  2048 |  9 | 3c1r2d | 24.059 | 0.094 | 0.2674 |               |
| `3c1r2d_mel_none_full`         | cosy16 |  8 | 80 Mel  | none         |  2048 |  9 | 3c1r2d | 26.979 | 0.106 | 0.2919 |               |
| `3c1r2d_mfcc_local`            | cosy15 |  8 | 80 MFCC | local        |  2048 | 10 | 3c1r2d | 25.261 | 0.098 | 0.2724 |               |
| `3c1r2d_mfcc_localscalar`      | cosy16 |  8 | 80 MFCC | local scalar |  2048 | 12 | 3c1r2d | 28.494 | 0.118 | 0.3235 |               |


### FB02TIITs04; V100 32GB
| train_dir                    | BS | Input   | Norm. | Units | Ep | Layout | Loss  | MED   | WER    | Notes                       |
|------------------------------|---:|---------|-------|------:|---:|-------:|------:|------:|-------:|-----------------------------|
| `3c1r2d_mel_local_full`      |  8 | 80 Mel  | local |  2048 | 20 | 3c4r2d | 25.43 | 0.083 | 0.2412 |                             |
| `3c3r2d_mel_local`           |  8 | 80 Mel  | local |  2048 | 11 | 3c3r2d | 17.32 | 0.062 | 0.1762 | Stopped early.              |
| `3c4r2d_mel_local_full_lstm` |  8 | 80 Mel  | local |  2048 |  5 | 3c4r2d | 11.849| 0.045 | 0.1264 | LSTM cells.                 |
| `3c5r2d_mel_local_full`      |  8 | 80 Mel  | local |  2048 |  9 | 3c5r2d | 13.26 | 0.044 | 0.1292 | LSTM cells. Server crashed. |
| `3c5r2d_mfcc_local_lstm_2`   | 16 | 80 MFCC | local |  2048 |  5 | 3c5r2d | 12.06 | 0.046 | 0.1271 | LSTM cells.                 |
| `3c4r2d_mel_local_tanh`      | 16 | 80 Mel  | local |  2048 |  9 | 3c4r2d | 25.58 | 0.113 | 0.308  | tanh RNN.                   |
| `3c4r2d_mel_local`           | 16 | 80 Mel  | local |  2048 |  x | 3c4r2d | xx.xx | 0.xxx | 0.xxx  | ReLU RNN.                   |


### FB11-NX-T02; 2xV100 16GB
| train_dir                     | BS | Input   | Norm. | Units | Ep | Layout | Loss  | MED   | WER    | Notes                      |
|-------------------------------|---:|---------|-------|------:|---:|-------:|------:|------:|-------:|----------------------------|
| `3c5r2d_mel_local_full_bs16`  | 16 | 80 Mel  | local |  2048 | 10 | 3c5r2d | 14.02 | 0.057 | 0.1583 | Stopped early.             |
| `3c5r2d_mfcc_local_full_bs16` | 16 | 80 MFCC | local |  2048 | 17 | 3c5r2d | 19.63 | 0.081 | 0.2207 | Tanh RNN.                  |
| `3c4r2d_mfcc_local_bs16_relu` | 16 | 80 MFCC | local |  2048 | 16 | 3c4r2d | 20.45 | 0.081 | 0.2273 | ReLU RNN. HDD full.        |
| `3c4r2d_mfcc_local_bs16_relu` | 16 | 80 MFCC | local |  2048 | 15 | 3c4r2d | 20.28 | 0.082 | 0.230  | ReLU RNN.                  |
| `3c4r2d_mel_local`            | 16 | 80 Mel  | local |  2048 |  9 | 3c4r2d | 17.42 | 0.068 | 0.194  | ReLU cells. For SortaGrad. |
| `3c2r2d_mel_local`            | 16 | 80 Mel  | local |  2048 | 12 | 3c2r2d | 18.19 | 0.076 | 0.215  | ReLU cells.                |


### FB11-NX-T01; 1xV100 16GB
| train_dir                      | BS | Input   | Norm. | Units | Ep | Layout | Loss  | MED   | WER    | Notes                     |
|--------------------------------|---:|---------|-------|------:|---:|-------:|------:|------:|-------:|---------------------------|
| `3c4r2d_mfcc_local_bs16_gru`   | 16 | 80 MFCC | local |  2048 | 10 | 3c4r2d | 16.78 | 0.067 | 0.1913 | GRU cells.                |
| `3c3r2d_mel_local_bs16_tanh`   | 16 | 80 Mel  | local |  2048 | 15 | 3c3r2d | 17.72 | 0.072 | 0.2059 | ReLU cells, despite name. |
| `3c4r2d_mel_local_nosortagrad` | 16 | 80 Mel  | local |  2048 | 15 | 3c4r2d | 17.89 | 0.070 | 0.2025 | ReLU cells. No SortaGrad. |



### Confidence Intervall Runs
| Run | ED    | WER   |
|----:|------:|------:|
| 1   | 0.290 | 0.709 |
| 2   | 0.301 | 0.727 |
| 3   | 0.300 | 0.724 |
| 4   | 0.297 | 0.724 |
| 5   | 0.290 | 0.703 |
| 6   | 0.301 | 0.721 |
| 7   | 0.295 | 0.715 |
| 8   | 0.275 | 0.733 |
| 9   | 0.291 | 0.708 |
| 10  | 0.291 | 0.703 |
| 11  | 0.294 | 0.705 |
| 12  | 0.290 | 0.699 |
| 13  | 0.292 | 0.710 |
| 14  | 0.294 | 0.718 |
| 15  | 0.295 | 0.708 |
| 16  | 0.299 | 0.714 |
| 17  | 0.296 | 0.722 |
| 18  | 0.296 | 0.712 |
| 19  | 0.290 | 0.706 |
| 20  | 0.298 | 0.718 |