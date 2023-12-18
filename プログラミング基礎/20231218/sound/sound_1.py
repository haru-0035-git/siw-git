# import winsound  
# # 音階の周波数（Hz） 
# frequencies  =  [261.63,  293.66,  329.63,  349.23,  392.00,  440.00,  493.88, 523.25] 
# # C4, D4, E4, F4, G4, A4, B4, C5  # 各音を1 秒間鳴らす 
# for freq in frequencies:     
#     winsound.Beep(int(freq), 1000) 

# import numpy as np 
# import pyaudio  # 音階の周波数（Hz） 
# frequencies = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88] # C4, D4, E4, F4, G4, A4, B4  
# # PyAudio の設定 
# fs = 44100  
# # サンプルレート 
# duration = 1.0  # 秒  
# # PyAudio オブジェクトの作成 
# p = pyaudio.PyAudio()  
# # ストリームの開始 
# stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)  
# # 各音階の正弦波を生成し、再生 
# for freq in frequencies:     
#     samples  =  (np.sin(2  *  np.pi  *  np.arange(fs  *  duration)  *  freq  /  fs)).astype(np.float32)
#     stream.write(samples.tobytes())  # ストリームの終了 
# stream.stop_stream() 
# stream.close()

#短形波
import numpy as np 
import pyaudio  
# パラメータ設定 
fs = 44100  # サンプルレート 
duration = 1.0  # 秒 
f = 440.0  # 周波数（Hz） 
volume = 0.5  # 音量（0.0 から1.0）  
# PyAudio オブジェクトの作成 
p = pyaudio.PyAudio()  
# ストリームの開始 
stream = p.open(format=pyaudio.paInt16, channels=1, rate=fs, output=True)  
# 矩形波の生成 
samples = (np.sign(np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)) * 32767 * volume).astype(np.int16)  
# 矩形波の再生 
stream.write(samples.tobytes())  
# ストリームの終了 
stream.stop_stream() 
stream.close()