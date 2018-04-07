"""
    NIH_EVENT
"""
import os
import datetime
import sys
import random
import Tkinter
import serial
import pygame
from nih_dialog import dialog

class App:
    """
        CLASS
    """
    def __init__(self):
        """
            FIRST_LOADED
        """
        pygame.init()
        self._running = True
        self._resume = []
        self._count_a = 0 # img_available_counter
        self._count_na = 0 # img_notAvaiable_counter
        self._resume_count = 0
        self._output_data_info = []
        self._output_data_img_available = []
        self._output_data_img_not_available = []
        self._output_data_white_available = []
        self._output_data_white_not_available = []
        self._output_data_resume_available = []
        self._output_data_resume_not_available = []
        self._output_data_baseline = []

        # SERIAL EVENT
        self._serial_event = ""
        self._sync_start = "5"
        self._sync_stop = "5"
        self._com_port = "COM1"
        self.init_serial()

        # TIMER (IN MS)
        self._img_timer = 5000
        self._resume_timer = 10000
        self._sleep_timer = 3000
        self._consigne_timer = 5000
        self._end_timer = 10000

        # WEIGHT OF IMG (ALWAYS 1)
        self._val = "1"

        # OUTPUT TXT FILES
        datetime_string = datetime.datetime.now().strftime("%d-%m-%Y_%Hh%Mm%Ss")
        current_directory = os.getcwd()
        if not os.path.exists(current_directory + "\\output\\" + datetime_string):
            os.makedirs(current_directory + "\\output\\" + datetime_string)
        self._output_txt_file_info = open("output\\" + datetime_string + "\\" + "NIH_INFO_" + datetime_string + ".txt", "w")
        self._output_txt_file_img_available = open("output\\" + datetime_string + "\\" + "NIH_IMG_AVAILABLE_" + datetime_string + ".txt", "w")
        self._output_txt_file_img_not_available = open("output\\" + datetime_string + "\\" + "NIH_IMG_NOT_AVAILABLE_" + datetime_string + ".txt", "w")
        self._output_txt_file_white_available = open("output\\" + datetime_string + "\\" + "NIH_WHITE_AVAILABLE_" + datetime_string + ".txt", "w")
        self._output_txt_file_white_not_available = open("output\\" + datetime_string + "\\" + "NIH_WHITE_NOT_AVAILABLE_" + datetime_string + ".txt", "w")
        self._output_txt_file_resume_available = open("output\\" + datetime_string + "\\" + "NIH_RESUME_AVAILABLE_" + datetime_string + ".txt", "w")
        self._output_txt_file_resume_not_available = open("output\\" + datetime_string + "\\" + "NIH_RESUME_NOT_AVAILABLE_" + datetime_string + ".txt", "w")
        self._output_txt_file_baseline = open("output\\" + datetime_string + "\\" + "NIH_BASELINE_" + datetime_string + ".txt", "w")

        # EXECUTE DIALOG BOX
        self.dialog_box()

        # INIT PYGAME
        pygame.display.init()
        pygame.mouse.set_visible(0)
        self._font_object = pygame.font.Font(None, 50)
        self._current_dir = os.getcwd() + "//"

        info_object = pygame.display.Info()
        self._size = (info_object.current_w, info_object.current_h)
        self._screen = pygame.display.set_mode(self._size, pygame.FULLSCREEN)
        self._seq_A = self.seq(0)
        self._seq_NA = self.seq(1)
        self._dispo = self.random_dispo()

        self._output_data_info.append(["Pygame timer resolution " + str(pygame.TIMER_RESOLUTION) + " ms"])
        # TIME 0 CALCUL + SEND SYNC
        self.send_event(self._sync_start) # SEND SYNC ON SERIAL PORT COM1 <-------------------------

####DEFINITIONS#####################################################################################

    def init_serial(self):
        """
            OPEN SERIAL PORT COM 1
        """
        print "OPEN COM1" 
        self._serial_event = serial.Serial(self._com_port, 9600, timeout=None)
        #self._serial_event = serial.Serial("COM1", 9600, timeout=None)
        if self._serial_event.isOpen(): # check whether it is open
            print 'Serial port COM1 open: ' + self._serial_event.portstr + ', baudrate: ' + str(self._serial_event.baudrate)
        else:
            print "Serial port COM1 close"

    def dialog_box(self):
        """
            SHOW DIALOG BOX AND RETRIEVE DATA
        """
        # Ask research participant info in a dialogbox
        root = Tkinter.Tk()
        root.withdraw()
        dialogInfo = dialog(root, 'Research participant information')
        root.quit()

        # Continue and print a summary if the research participant form has been correctly completed
        # Leave otherwise
        try:
            subjectInfo = 'Research participant information summary: \n' + 'First name: ' + dialogInfo.firstName + '\n' + 'Last name: ' + dialogInfo.lastName + '\n'

            self._output_data_info.append([subjectInfo])
        except:
            print "Could not retrieve information from the research participant window\n"
            self.on_exit()

    def random_dispo(self):
        """
            RAND DISPO/NON_DISPO
        """
        dispo = random.randrange(0, 2, 1)
        if dispo == 0:
            return False
        elif dispo == 1:
            return True

    def seq(self, i):
        """
            SEQ_img Available - Not Available
        """
        if i == 0:
            self._seq_A = ['img_5.png', 'img_19.png', 'img_25.png', 'img_27.png', 'img_20.png', 'img_14.png', 'img_4.png', 'img_50.png', 'img_6.png', 'img_35.png', 'img_36.png', 'img_11.png', 'img_37.png', 'img_41.png', 'img_21.png', 'img_38.png', 'img_40.png', 'img_24.png', 'img_22.png', 'img_48.png', 'img_8.png', 'img_29.png', 'img_32.png', 'img_47.png', 'img_33.png', 'img_49.png', 'img_42.png', 'img_12.png', 'img_43.png', 'img_3.png', 'img_9.png', 'img_10.png', 'img_18.png', 'img_16.png', 'img_1.png', 'img_23.png', 'img_34.png', 'img_26.png', 'img_46.png', 'img_31.png', 'img_44.png', 'img_7.png', 'img_39.png', 'img_2.png', 'img_15.png', 'img_45.png', 'img_30.png', 'img_17.png', 'img_28.png', 'img_13.png']
            return self._seq_A

        elif i == 1:
            self._seq_NA = ['img_41.png', 'img_40.png', 'img_7.png', 'img_14.png', 'img_39.png', 'img_24.png', 'img_26.png', 'img_17.png', 'img_1.png', 'img_34.png', 'img_22.png', 'img_30.png', 'img_12.png', 'img_18.png', 'img_2.png', 'img_25.png', 'img_23.png', 'img_8.png', 'img_9.png', 'img_11.png', 'img_5.png', 'img_38.png', 'img_43.png', 'img_48.png', 'img_35.png', 'img_47.png', 'img_45.png', 'img_28.png', 'img_37.png', 'img_13.png', 'img_19.png', 'img_4.png', 'img_49.png', 'img_10.png', 'img_44.png', 'img_50.png', 'img_42.png', 'img_29.png', 'img_3.png', 'img_6.png', 'img_27.png', 'img_20.png', 'img_46.png', 'img_36.png', 'img_33.png', 'img_32.png', 'img_21.png', 'img_15.png', 'img_31.png', 'img_16.png']
            return self._seq_NA

        #seq_test = ['img_1.png', 'img_2.png', 'img_3.png', 'img_4.png', 'img_5.png', 'img_6.png', 'img_7.png', 'img_8.png', 'img_9.png', 'img_10.png', 'img_11.png', 'img_12.png', 'img_13.png', 'img_14.png', 'img_15.png', 'img_16.png', 'img_17.png', 'img_18.png', 'img_19.png', 'img_20.png', 'img_21.png', 'img_22.png', 'img_23.png', 'img_24.png', 'img_25.png', 'img_26.png', 'img_27.png', 'img_28.png', 'img_29.png', 'img_30.png', 'img_31.png', 'img_32.png', 'img_33.png', 'img_34.png', 'img_35.png', 'img_36.png', 'img_37.png', 'img_38.png', 'img_39.png', 'img_40.png', 'img_41.png', 'img_42.png', 'img_43.png', 'img_44.png', 'img_45.png', 'img_46.png', 'img_47.png', 'img_48.png', 'img_49.png', 'img_50.png']

    def random_sleep(self):
        """
            RANDOM_SLEEP
        """
        rand_sleep = random.randrange(0, 1200, 1)
        sleep = 1800 + rand_sleep
        return sleep

    def white_screen(self):
        """
            WHITE_SCREEN
        """
        self._screen.fill((255, 255, 255))
        pygame.display.update()

    def consigne_img_dispo(self):
        """
            DISPLAY CONSIGNES_IMG DISPO
        """
        img = pygame.image.load(self._current_dir + "CONSIGNE_DISPO.png").convert()
        img_dest = img.get_rect(centerx=(self._screen.get_width())/2, centery=(self._screen.get_height())/2)
        self._screen.blit(img, img_dest)
        pygame.display.update()

    def consigne_img_ndispo(self):
        """
            DISPLAY CONSIGNES_IMG NON_DISPO
        """
        img = pygame.image.load(self._current_dir + "CONSIGNE_NON_DISPO.png").convert()
        img_dest = img.get_rect(centerx=(self._screen.get_width())/2, centery=(self._screen.get_height())/2)
        self._screen.blit(img, img_dest)
        pygame.display.update()

    def match_img_ndispo(self):
        """
            DISPLAY MATCH_IMG NON_DISPO
        """
        img = pygame.image.load(self._current_dir + self._seq_NA[self._count_na]).convert()
        self._resume.insert(self._resume_count, img)
        img_dest = img.get_rect(centerx=(self._screen.get_width())/2, centery=(self._screen.get_height())/2)
        self._screen.blit(img, img_dest)
        pygame.display.update()

    def match_img_dispo(self):
        """
            DISPLAY MATCH_IMG DISPO
        """
        img = pygame.image.load(self._current_dir + self._seq_A[self._count_a]).convert()
        self._resume.insert(self._resume_count, img)
        img_dest = img.get_rect(centerx=(self._screen.get_width())/2, centery=(self._screen.get_height())/2)
        self._screen.blit(img, img_dest)
        pygame.display.update()

    def resume(self):
        """
            DISPLAY SUMARY IMG + CONSIGNES
        """
        consigne = self._font_object.render("OVERVIEW", 1, (0, 0, 0))
        consigne_dest = consigne.get_rect(centerx=(self._screen.get_width())/2, centery=(self._screen.get_height())*0.1)
        self._screen.blit(consigne, consigne_dest)
        i = 0
        for img in self._resume:
            if i == 0:
                img_dest0 = (self._size[0]*0, self._size[1]*0.2)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest0)
                num_0 = self._font_object.render("1", 1, (0, 0, 0))
                num_dest_0 = num_0.get_rect(centerx=self._size[0]*0.1, centery=self._size[1]*0.2)
                self._screen.blit(num_0, num_dest_0)

            elif i == 1:
                img_dest1 = (self._size[0]*0.2, self._size[1]*0.2)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest1)
                num_1 = self._font_object.render("2", 1, (0, 0, 0))
                num_dest_1 = num_1.get_rect(centerx=self._size[0]*0.3, centery=self._size[1]*0.2)
                self._screen.blit(num_1, num_dest_1)

            elif i == 2:
                img_dest2 = (self._size[0]*0.4, self._size[1]*0.2)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest2)
                num_2 = self._font_object.render("3", 1, (0, 0, 0))
                num_dest_2 = num_2.get_rect(centerx=self._size[0]*0.5, centery=self._size[1]*0.2)
                self._screen.blit(num_2, num_dest_2)

            elif i == 3:
                img_dest3 = (self._size[0]*0.6, self._size[1]*0.2)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest3)
                num_3 = self._font_object.render("4", 1, (0, 0, 0))
                num_dest_3 = num_3.get_rect(centerx=self._size[0]*0.7, centery=self._size[1]*0.2)
                self._screen.blit(num_3, num_dest_3)

            elif i == 4:
                img_dest4 = (self._size[0]*0.8, self._size[1]*0.2)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest4)
                num_4 = self._font_object.render("5", 1, (0, 0, 0))
                num_dest_4 = num_4.get_rect(centerx=self._size[0]*0.9, centery=self._size[1]*0.2)
                self._screen.blit(num_4, num_dest_4)

            elif i == 5:
                img_dest5 = (self._size[0]*0, self._size[1]*0.6)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest5)
                num_5 = self._font_object.render("6", 1, (0, 0, 0))
                num_dest_5 = num_0.get_rect(centerx=self._size[0]*0.1, centery=self._size[1]*0.6)
                self._screen.blit(num_5, num_dest_5)

            elif i == 6:
                img_dest6 = (self._size[0]*0.2, self._size[1]*0.6)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest6)
                num_6 = self._font_object.render("7", 1, (0, 0, 0))
                num_dest_6 = num_6.get_rect(centerx=self._size[0]*0.3, centery=self._size[1]*0.6)
                self._screen.blit(num_6, num_dest_6)

            elif i == 7:
                img_dest7 = (self._size[0]*0.4, self._size[1]*0.6)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest7)
                num_7 = self._font_object.render("8", 1, (0, 0, 0))
                num_dest_7 = num_2.get_rect(centerx=self._size[0]*0.5, centery=self._size[1]*0.6)
                self._screen.blit(num_7, num_dest_7)

            elif i == 8:
                img_dest8 = (self._size[0]*0.6, self._size[1]*0.6)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest8)
                num_8 = self._font_object.render("9", 1, (0, 0, 0))
                num_dest_8 = num_3.get_rect(centerx=self._size[0]*0.7, centery=self._size[1]*0.6)
                self._screen.blit(num_8, num_dest_8)

            else:
                img_dest9 = (self._size[0]*0.8, self._size[1]*0.6)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest9)
                num_9 = self._font_object.render("10", 1, (0, 0, 0))
                num_dest_9 = num_9.get_rect(centerx=self._size[0]*0.9, centery=self._size[1]*0.6)
                self._screen.blit(num_9, num_dest_9)

            i += 1
        pygame.display.update()

    def output_txt_file(self):
        """
            OUTPUT TEXT IN 3 COLUMN (START, STOP, VAL)
        """
        # INFO
        for row in self._output_data_info:
            for item in row:
                self._output_txt_file_info.write(item.ljust(1) + "\t")
            self._output_txt_file_info.write("\n")
        self._output_txt_file_info.close()

        # IMG
        for row in self._output_data_img_available:
            for item in row:
                self._output_txt_file_img_available.write(item.ljust(1) + "\t")
            self._output_txt_file_img_available.write("\n")
        self._output_txt_file_img_available.close()

        for row in self._output_data_img_not_available:
            for item in row:
                self._output_txt_file_img_not_available.write(item.ljust(1) + "\t")
            self._output_txt_file_img_not_available.write("\n")
        self._output_txt_file_img_not_available.close()

        # WHITE
        for row in self._output_data_white_available:
            for item in row:
                self._output_txt_file_white_available.write(item.ljust(1) + "\t")
            self._output_txt_file_white_available.write("\n")
        self._output_txt_file_white_available.close()

        for row in self._output_data_white_not_available:
            for item in row:
                self._output_txt_file_white_not_available.write(item.ljust(1) + "\t")
            self._output_txt_file_white_not_available.write("\n")
        self._output_txt_file_white_not_available.close()

        # RESUME
        for row in self._output_data_resume_available:
            for item in row:
                self._output_txt_file_resume_available.write(item.ljust(1) + "\t")
            self._output_txt_file_resume_available.write("\n")
        self._output_txt_file_resume_available.close()

        for row in self._output_data_resume_not_available:
            for item in row:
                self._output_txt_file_resume_not_available.write(item.ljust(1) + "\t")
            self._output_txt_file_resume_not_available.write("\n")
        self._output_txt_file_resume_not_available.close()

        # BASELINE
        for row in self._output_data_baseline:
            for item in row:
                self._output_txt_file_baseline.write(item.ljust(1) + "\t")
            self._output_txt_file_baseline.write("\n")
        self._output_txt_file_baseline.close()

####EXECUTIONS######################################################################################

    def on_execute(self):
        """
           MAIN WORK
        """
        # int = nbr. images
        run = True
        while run:
            if self._dispo is True and self._count_a < len(self._seq_A):
                self.white_screen()
                self.consigne_img_dispo()
                self.on_event(self._consigne_timer)
                self.white_screen()
                self._resume = []
                self._resume_count = 0
                for self._resume_count in range(0, 10, 1): # BLOC 10 IMG AVAILABLE
                    self.match_img_dispo() #SHOW IMG
                    start_img = (pygame.time.get_ticks()-self._clock_time_zero)/1000
                    self.on_event(self._img_timer)
                    self.white_screen()
                    stop_img_start_white = (pygame.time.get_ticks()-self._clock_time_zero)/1000
                    self.on_event(self.random_sleep())
                    stop_white = (pygame.time.get_ticks()-self._clock_time_zero)/1000
                    self._output_data_img_available.append([str(start_img), str(stop_img_start_white), str(self._val)]) # TIMER OUTPUT IMG AVAILABLE
                    self._output_data_white_available.append([str(stop_img_start_white), str(stop_white), str(self._val)]) # TIMER OUTPUT WHITE SCREEN AVAILABLE
                    self._count_a += 1
                    if self._resume_count == 9:
                        self.resume()
                        start_resume = (pygame.time.get_ticks()-self._clock_time_zero)/1000
                        self.on_event(self._resume_timer)
                        self.white_screen()
                        stop_resume_start_baseline = (pygame.time.get_ticks()-self._clock_time_zero)/1000
                        self._output_data_resume_available.append([str(start_resume), str(stop_resume_start_baseline), str(self._val)]) # TIMER OUTPUT RESUME AVAILABLE
                self._dispo = False
                self.on_event(self._end_timer)
                stop_baseLine = (pygame.time.get_ticks()-self._clock_time_zero)/1000
                self._output_data_baseline.append([str(stop_resume_start_baseline), str(stop_baseLine), str(self._val)]) # TIMER OUTPUT BASELINE

            elif self._dispo is False and self._count_na < len(self._seq_NA):
                self.white_screen()
                self.consigne_img_ndispo() #SHOW IMG
                self.on_event(self._consigne_timer)
                self.white_screen()
                self._resume = []
                self._resume_count = 0
                for self._resume_count in range(0, 10, 1): # BLOC 10 IMG NON AVAILABLE
                    self.match_img_ndispo()
                    start_img = (pygame.time.get_ticks()-self._clock_time_zero)/1000
                    self.on_event(self._img_timer)
                    self.white_screen()
                    stop_img_start_white = (pygame.time.get_ticks()-self._clock_time_zero)/1000
                    self.on_event(self.random_sleep())
                    stop_white = (pygame.time.get_ticks()-self._clock_time_zero)/1000
                    self._output_data_img_not_available.append([str(start_img), str(stop_img_start_white), str(self._val)]) # TIMER OUTPUT IMG NOT AVAILABLE
                    self._output_data_white_not_available.append([str(stop_img_start_white), str(stop_white), str(self._val)]) # TIMER OUTPUT WHITE SCREEN NOT AVAILABLE
                    self._count_na += 1
                    if self._resume_count == 9:
                        self.resume()
                        start_resume = (pygame.time.get_ticks()-self._clock_time_zero)/1000
                        self.on_event(self._resume_timer)
                        self.white_screen()
                        stop_resume_start_baseline = (pygame.time.get_ticks()-self._clock_time_zero)/1000
                        self._output_data_resume_not_available.append([str(start_resume), str(stop_resume_start_baseline), str(self._val)]) # TIMER OUTPUT RESUME AVAILABLE
                self._dispo = True
                self.on_event(self._end_timer)
                stop_baseLine = (pygame.time.get_ticks()-self._clock_time_zero)/1000
                self._output_data_baseline.append([str(stop_resume_start_baseline), str(stop_baseLine), str(self._val)]) # TIMER OUTPUT BASELINE

            elif self._count_a == len(self._seq_A) and self._count_na == len(self._seq_NA):
                self._output_data_info.append(["EXIT OK"])
                consigne = self._font_object.render("Merci de votre participation a cette experience...", 1, (0, 0, 0))
                consigne_dest = consigne.get_rect(centerx=(self._screen.get_width())/2, centery=(self._screen.get_height())/2)
                self._screen.blit(consigne, consigne_dest)
                pygame.display.update()
                self.on_event(self._sleep_timer)
                run = False
                self.on_exit()

            else:
                self._output_data_info.append(["ERROR DURING RUN"])

    def on_exit(self):
        """
           EXIT WORK
        """
        clock_time_end = pygame.time.get_ticks()
        self._output_data_info.append(["Temps fin " + str(clock_time_end) + " ms"])
        self.send_event(self._sync_stop) # SEND SYNC ON SERIAL PORT COM1
        self.output_txt_file()
        self._serial_event.close()
        pygame.display.quit()
        pygame.quit()
        sys.exit()

####EVENTS##########################################################################################

    def send_event(self, num):
        """
            SEND EVENT ON SERIAL PORT
        """
        # Modified code from thread reading the serial port
        print "Waiting for SYNC"
        tdata = self._serial_event.read()
		
        print tdata
        if tdata == "5":
            self._clock_time_zero = pygame.time.get_ticks() # TIME ZERO
            self._output_data_info.append(["Temps zero " + str(self._clock_time_zero) + " ms"])
            print 'SYNC OK'

        print "END SYNC"
    def on_event(self, time):
        """
            KEYDOWN EVENT
        """
        pygame.event.clear(pygame.KEYDOWN) # Remove non desired KEYDOWN EVENT
        timeout = pygame.time.get_ticks()-self._clock_time_zero + time
        on_event_ok = True
        while on_event_ok:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._output_data_info.append(["MANUAL EXIT"])
                        on_event_ok = False
                        self.on_exit()

            if pygame.time.get_ticks()-self._clock_time_zero > timeout:
                on_event_ok = False

####################################################################################################

if __name__ == "__main__":
    THE_APP = App()
    THE_APP.on_execute()
