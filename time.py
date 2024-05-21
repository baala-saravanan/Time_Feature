from subprocess import check_output
import vlc
import os
import time
import math
import subprocess
from pydub import AudioSegment
import sys
sys.path.insert(0, '/home/rock/Desktop/Hearsight/')
from play_audio import GTTSA
play_audio = GTTSA()
            
class Tind:

    def tellTime(self):
        try:
            a = check_output(['sudo','hwclock','-r','-f','/dev/rtc1'])
            b = a.decode("utf-8")
            hour = int(b[11:13])
            minute = int(b[14:16])

            if hour >= 12:
                period_audio = "pm.mp3"
                hour -= 12
                if hour == 0:
                    hour = 12
            else:
                period_audio = "am.mp3"

            play_audio.play_machine_audio("time.mp3")
            print("Time")

            play_audio.play_machine_audio(f"number_{str(hour)}.mp3")
    #       play_audio.play_machine_audioio("hours.mp3")

            tens_minutes_audio = f"number_{str(minute)}.mp3"
            
            if tens_minutes_audio != "0" and tens_minutes_audio != "00":  
                play_audio.play_machine_audio(tens_minutes_audio)
                
    #       play_audio.play_machine_audioio("minutes.mp3")
            play_audio.play_machine_audio(period_audio)

            play_audio.play_machine_audio("date.mp3")
            print("Date")

            # date
            day = int(b[8:10])
            month = int(b[5:7])
            year = int(b[0:4])
            
            
            year_th = 2000
            year_tens = year - year_th 
            
            day_tens = int(day // 10) * 10
            day_ones = int(day % 10)
            
            play_audio.play_machine_audio(f"number_{str(day)}.mp3")
            #play_audio.play_machine_audioio(f"number_{str(day_ones)}.mp3")
            play_audio.play_machine_audio(f"number_{str(month)}.mp3")
            

            year_tens_audio = f"number_{str(year_tens)}.mp3"
            play_audio.play_machine_audio(year_tens_audio)
            
    #        year_ones_audio = f"number_{str(year_ones)}.mp3"
    #        play_audio.play_machine_audioio(year_ones_audio)
        except Exception as e:
#            play_audio.play_machine_audio("error in time module.mp3")
#            play_audio.play_machine_audio("so_switch_off_the_HearSight_device_for_some_time_and_then_start_it_again.mp3")
            print(f"Error in time module: {e}")
            play_audio.play_machine_audio("hold_on_connection_in_progress_initiating_shortly.mp3")
            play_audio.play_machine_audio("Thank You.mp3")
            subprocess.run(["reboot"])
            return
#            print(f"Error in time module: {e}")
            
if __name__ == "__main__":
    tind = Tind()
