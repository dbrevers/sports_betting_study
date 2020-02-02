####
###		Sports betting task designed by D. Brevers
##		Programmed by M. Petieau in February 2019 based on a previous Python 2.7 task developed by D. Verdonck
#

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
        self._count_WE1 = 0 # img_WE1_counter
        self._count_WE2 = 0 # img_W2_counter
        self._resume_count = 0
        self._output_data_info = []
        self._output_data_img_noFrame_WE1_green = []
        self._output_data_img_noFrame_WE1_red = []
        self._output_data_img_frame_WE1_green = []
        self._output_data_img_frame_WE1_red = []
        self._output_data_img_noFrame_WE2_green = []
        self._output_data_img_noFrame_WE2_red = []
        self._output_data_img_frame_WE2_green = []
        self._output_data_img_frame_WE2_red = []
        self._output_data_white_WE1_green = []
        self._output_data_white_WE1_red = []
        self._output_data_white_WE2_green = []
        self._output_data_white_WE2_red = []
        self._output_data_white_pre_WE1_green = []
        self._output_data_white_pre_WE1_red = []
        self._output_data_white_pre_WE2_green = []
        self._output_data_white_pre_WE2_red = []
        self._output_data_resume_WE1 = []
        self._output_data_resume_WE2 = []
        self._output_data_baseline = []
        self._output_data_img_frame_WE1_WE2_green = []
        self._output_data_img_frame_WE1_WE2_red = []
        self._output_data_img_noFrame_WE1_WE2_green = []
        self._output_data_img_noFrame_WE1_WE2_red = []

        # SERIAL EVENT
        self._serial_event = ""
        self._sync_start = "5"
        self._sync_stop = "5"
        self._com_port = "COM1"
        self.init_serial()

        # TIMER (IN MS)
        self._img_timer = 2000
        self._img_frame_timer = 5000
        self._resume_timer = 8000
        self._sleep_timer = 3000
        self._consigne_timer = 3000
        self._end_timer = 3000

        # WEIGHT OF IMG (ALWAYS 1)
        self._val = "1"

        # OUTPUT TXT FILES
        datetime_string = datetime.datetime.now().strftime("%d-%m-%Y_%Hh%Mm%Ss")
        current_directory = os.getcwd()
        if not os.path.exists(current_directory + "\\output\\" + datetime_string):
            os.makedirs(current_directory + "\\output\\" + datetime_string)
        self._output_txt_file_info = open("output\\" + datetime_string + "\\" + "NIH_INFO_" + datetime_string + ".txt", "w")
        self._output_txt_file_img_noFrame_WE1_green = open("output\\" + datetime_string + "\\" + "NIH_IMG_NOFRAME_WE1_GREEN_" + datetime_string + ".txt", "w")
        self._output_txt_file_img_noFrame_WE1_red = open("output\\" + datetime_string + "\\" + "NIH_IMG_NOFRAME_WE1_RED_" + datetime_string + ".txt", "w")
        self._output_txt_file_img_frame_WE1_green = open("output\\" + datetime_string + "\\" + "NIH_IMG_FRAME_WE1_GREEN_" + datetime_string + ".txt", "w")
        self._output_txt_file_img_frame_WE1_red = open("output\\" + datetime_string + "\\" + "NIH_IMG_FRAME_WE1_RED_" + datetime_string + ".txt", "w")
        self._output_txt_file_img_frame_WE2_green = open("output\\" + datetime_string + "\\" + "NIH_IMG_FRAME_WE2_GREEN_" + datetime_string + ".txt", "w")
        self._output_txt_file_img_frame_WE2_red = open("output\\" + datetime_string + "\\" + "NIH_IMG_FRAME_WE2_RED_" + datetime_string + ".txt", "w")
        self._output_txt_file_img_noFrame_WE2_green = open("output\\" + datetime_string + "\\" + "NIH_IMG_NOFRAME_WE2_GREEN_" + datetime_string + ".txt", "w")
        self._output_txt_file_img_noFrame_WE2_red = open("output\\" + datetime_string + "\\" + "NIH_IMG_NOFRAME_WE2_RED_" + datetime_string + ".txt", "w")
        self._output_txt_file_white_WE1_green = open("output\\" + datetime_string + "\\" + "NIH_WHITE_WE1_GREEN_" + datetime_string + ".txt", "w")
        self._output_txt_file_white_WE1_red = open("output\\" + datetime_string + "\\" + "NIH_WHITE_WE1_RED_" + datetime_string + ".txt", "w")
        self._output_txt_file_white_WE2_green = open("output\\" + datetime_string + "\\" + "NIH_WHITE_WE2_GREEN_" + datetime_string + ".txt", "w")
        self._output_txt_file_white_WE2_red = open("output\\" + datetime_string + "\\" + "NIH_WHITE_WE2_RED_" + datetime_string + ".txt", "w")
        self._output_txt_file_white_pre_WE1_green = open("output\\" + datetime_string + "\\" + "NIH_WHITE_PRE_WE1_GREEN_" + datetime_string + ".txt", "w")
        self._output_txt_file_white_pre_WE1_red = open("output\\" + datetime_string + "\\" + "NIH_WHITE_PRE_WE1_RED_" + datetime_string + ".txt", "w")
        self._output_txt_file_white_pre_WE2_green = open("output\\" + datetime_string + "\\" + "NIH_WHITE_PRE_WE2_GREEN_" + datetime_string + ".txt", "w")
        self._output_txt_file_white_pre_WE2_red = open("output\\" + datetime_string + "\\" + "NIH_WHITE_PRE_WE2_RED_" + datetime_string + ".txt", "w")
        self._output_txt_file_resume_WE1 = open("output\\" + datetime_string + "\\" + "NIH_RESUME_WE1_" + datetime_string + ".txt", "w")
        self._output_txt_file_resume_WE2 = open("output\\" + datetime_string + "\\" + "NIH_RESUME_WE2_" + datetime_string + ".txt", "w")
        self._output_txt_file_baseline = open("output\\" + datetime_string + "\\" + "NIH_BASELINE_" + datetime_string + ".txt", "w")
        self._output_txt_file_img_frame_WE1_WE2_green = open("output\\" + datetime_string + "\\" + "NIH_IMG_FRAME_WE1_WE2_GREEN_" + datetime_string + ".txt", "w")
        self._output_txt_file_img_frame_WE1_WE2_red = open("output\\" + datetime_string + "\\" + "NIH_IMG_FRAME_WE1_WE2_RED_" + datetime_string + ".txt", "w")
        self._output_txt_file_img_noFrame_WE1_WE2_green = open("output\\" + datetime_string + "\\" + "NIH_IMG_NOFRAME_WE1_WE2_GREEN_" + datetime_string + ".txt", "w")
        self._output_txt_file_img_noFrame_WE1_WE2_red = open("output\\" + datetime_string + "\\" + "NIH_IMG_NOFRAME_WE1_WE2_RED_" + datetime_string + ".txt", "w")

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
        self._seq_WE1 = self.seq(0)
        self._seq_WE2 = self.seq(1)
        self._frame_seq = self.seq(2)
        self._WE = self.random_WE()

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
        if self._serial_event.isOpen(): # check whether it is open
            print 'Serial port COM1 open: ' + self._serial_event.portstr + ', baudrate: ' + str(self._serial_event.baudrate)
        else:
            print "Serial port COM1 close"

    def dialog_box(self):
        """
            SHOW DIALOG BOX AND RETRIEVE DATA
        """
        # Ask participant info in a dialogbox
        root = Tkinter.Tk()
        root.withdraw()
        dialogInfo = dialog(root, 'Participant information')
        root.quit()

        # Continue and print a summary if the participant form has been correctly completed
        # Leave otherwise
        try:
            subjectInfo = 'Participant information summary: \n' + 'First name: ' + dialogInfo.firstName + '\n' + 'Last name: ' + dialogInfo.lastName + '\n'

            self._output_data_info.append([subjectInfo])
        except:
            print "Could not retrieve information from the participant window\n"
            self.on_exit()

    def random_WE(self):
        """
            RAND WE1/WE2
        """
        WE = random.randrange(0, 2, 1)
        if WE == 0:
            return False
        elif WE == 1:
            return True

    def seq(self, i):
        """
            SEQ_img WE1 - WE2
        """
        if i == 0:
            self._seq_WE1 = ['img_5.png', 'img_19.png', 'img_25.png', 'img_27.png', 'img_20.png', 'img_14.png', 'img_4.png', 'img_50.png', 'img_6.png', 'img_35.png', \
                           'img_36.png', 'img_11.png', 'img_37.png', 'img_41.png', 'img_21.png', 'img_38.png', 'img_40.png', 'img_24.png', 'img_22.png', 'img_48.png', \
                           'img_8.png', 'img_29.png', 'img_32.png', 'img_47.png', 'img_33.png', 'img_49.png', 'img_42.png', 'img_12.png', 'img_43.png', 'img_3.png', \
                           'img_9.png', 'img_10.png', 'img_18.png', 'img_16.png', 'img_1.png', 'img_23.png', 'img_34.png', 'img_26.png', 'img_46.png', 'img_31.png', \
                           'img_44.png', 'img_7.png', 'img_39.png', 'img_2.png', 'img_15.png', 'img_45.png', 'img_30.png', 'img_17.png', 'img_28.png', 'img_13.png']
            return self._seq_WE1

        elif i == 1:
            self._seq_WE2 = ['img_91.png', 'img_90.png', 'img_57.png', 'img_64.png', 'img_89.png', 'img_74.png', 'img_76.png', 'img_67.png', 'img_51.png', 'img_84.png', \
                            'img_72.png', 'img_80.png', 'img_62.png', 'img_68.png', 'img_52.png', 'img_75.png', 'img_73.png', 'img_58.png', 'img_59.png', 'img_61.png', \
                            'img_55.png', 'img_88.png', 'img_93.png', 'img_98.png', 'img_85.png', 'img_97.png', 'img_95.png', 'img_78.png', 'img_87.png', 'img_63.png', \
                            'img_69.png', 'img_54.png', 'img_99.png', 'img_60.png', 'img_94.png', 'img_100.png', 'img_92.png', 'img_79.png', 'img_53.png', 'img_56.png', \
                            'img_77.png', 'img_70.png', 'img_96.png', 'img_86.png', 'img_83.png', 'img_82.png', 'img_71.png', 'img_65.png', 'img_81.png', 'img_66.png']
            return self._seq_WE2

        # Define frame color for each bloc and each trial (1=green, 0=red) - M. Petieau - February 2019
        elif i == 2:
            self._frame_seq = [0, 1, 1, 0, 1, 0, 1, 0, 0, 1, \
                               1, 0, 1, 1, 0, 0, 1, 0, 1, 0, \
                               0, 1, 0, 0, 1, 0, 1, 0, 0, 1, \
                               1, 0, 0, 0, 1, 0, 1, 1, 0, 1, \
                               1, 1, 0, 1, 0, 1, 1, 0, 0, 1]
            return self._frame_seq

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

    def consigne_img_WE1(self):
        """
            DISPLAY CONSIGNES_IMG WE1
        """
        img = pygame.image.load(self._current_dir + "CONSIGNE_WE1.png").convert()
        img_dest = img.get_rect(centerx=(self._screen.get_width())/2, centery=(self._screen.get_height())/2)
        self._screen.blit(img, img_dest)
        pygame.display.update()

    def consigne_img_WE2(self):
        """
            DISPLAY CONSIGNES_IMG WE2
        """
        img = pygame.image.load(self._current_dir + "CONSIGNE_WE2.png").convert()
        img_dest = img.get_rect(centerx=(self._screen.get_width())/2, centery=(self._screen.get_height())/2)
        self._screen.blit(img, img_dest)
        pygame.display.update()

    def match_img_WE2(self,addInResume):
        """
            DISPLAY MATCH_IMG WE2
        """
        img = pygame.image.load(self._current_dir + self._seq_WE2[self._count_WE2]).convert()
        if addInResume == 1:
            self._resume.insert(self._resume_count, img)
        img_dest = img.get_rect(centerx=(self._screen.get_width())/2, centery=(self._screen.get_height())/2)
        self._screen.blit(img, img_dest)
        pygame.display.update()

    def match_img_WE1(self,addInResume):
        """
            DISPLAY MATCH_IMG WE1
        """
        img = pygame.image.load(self._current_dir + self._seq_WE1[self._count_WE1]).convert()
        if addInResume == 1:
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
                img_dest0 = (self._size[0]*0.12, self._size[1]*0.2)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest0)
                num_0 = self._font_object.render("1", 1, (0, 0, 0))
                num_dest_0 = num_0.get_rect(centerx=self._size[0]*0.20, centery=self._size[1]*0.2)
                self._screen.blit(num_0, num_dest_0)

            elif i == 1:
                img_dest1 = (self._size[0]*0.42, self._size[1]*0.2)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest1)
                num_1 = self._font_object.render("2", 1, (0, 0, 0))
                num_dest_1 = num_1.get_rect(centerx=self._size[0]*0.50, centery=self._size[1]*0.2)
                self._screen.blit(num_1, num_dest_1)

            elif i == 2:
                img_dest2 = (self._size[0]*0.72, self._size[1]*0.2)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest2)
                num_2 = self._font_object.render("3", 1, (0, 0, 0))
                num_dest_2 = num_2.get_rect(centerx=self._size[0]*0.80, centery=self._size[1]*0.2)
                self._screen.blit(num_2, num_dest_2)

            elif i == 3:
                img_dest3 = (self._size[0]*0.27, self._size[1]*0.6)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest3)
                num_3 = self._font_object.render("4", 1, (0, 0, 0))
                num_dest_3 = num_3.get_rect(centerx=self._size[0]*0.33, centery=self._size[1]*0.6)
                self._screen.blit(num_3, num_dest_3)

            elif i == 4:
                img_dest4 = (self._size[0]*0.57, self._size[1]*0.6)
                self._screen.blit(pygame.transform.scale(img, ((self._size[0]/5), (self._size[1]/3))), img_dest4)
                num_4 = self._font_object.render("5", 1, (0, 0, 0))
                num_dest_4 = num_4.get_rect(centerx=self._size[0]*0.63, centery=self._size[1]*0.6)
                self._screen.blit(num_4, num_dest_4)

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
        for row in self._output_data_img_noFrame_WE1_green:
            for item in row:
                self._output_txt_file_img_noFrame_WE1_green.write(item.ljust(1) + "\t")
            self._output_txt_file_img_noFrame_WE1_green.write("\n")
        self._output_txt_file_img_noFrame_WE1_green.close()

        for row in self._output_data_img_noFrame_WE1_red:
            for item in row:
                self._output_txt_file_img_noFrame_WE1_red.write(item.ljust(1) + "\t")
            self._output_txt_file_img_noFrame_WE1_red.write("\n")
        self._output_txt_file_img_noFrame_WE1_red.close()

        for row in self._output_data_img_noFrame_WE2_green:
            for item in row:
                self._output_txt_file_img_noFrame_WE2_green.write(item.ljust(1) + "\t")
            self._output_txt_file_img_noFrame_WE2_green.write("\n")
        self._output_txt_file_img_noFrame_WE2_green.close()

        for row in self._output_data_img_noFrame_WE2_red:
            for item in row:
                self._output_txt_file_img_noFrame_WE2_red.write(item.ljust(1) + "\t")
            self._output_txt_file_img_noFrame_WE2_red.write("\n")
        self._output_txt_file_img_noFrame_WE2_red.close()

        for row in self._output_data_img_noFrame_WE1_WE2_green:
            for item in row:
                self._output_txt_file_img_noFrame_WE1_WE2_green.write(item.ljust(1) + "\t")
            self._output_txt_file_img_noFrame_WE1_WE2_green.write("\n")
        self._output_txt_file_img_noFrame_WE1_WE2_green.close()

        for row in self._output_data_img_noFrame_WE1_WE2_red:
            for item in row:
                self._output_txt_file_img_noFrame_WE1_WE2_red.write(item.ljust(1) + "\t")
            self._output_txt_file_img_noFrame_WE1_WE2_red.write("\n")
        self._output_txt_file_img_noFrame_WE1_WE2_red.close()

        # IMG FRAME
        for row in self._output_data_img_frame_WE1_green:
            for item in row:
                self._output_txt_file_img_frame_WE1_green.write(item.ljust(1) + "\t")
            self._output_txt_file_img_frame_WE1_green.write("\n")
        self._output_txt_file_img_frame_WE1_green.close()

        for row in self._output_data_img_frame_WE1_red:
            for item in row:
                self._output_txt_file_img_frame_WE1_red.write(item.ljust(1) + "\t")
            self._output_txt_file_img_frame_WE1_red.write("\n")
        self._output_txt_file_img_frame_WE1_red.close()

        for row in self._output_data_img_frame_WE2_green:
            for item in row:
                self._output_txt_file_img_frame_WE2_green.write(item.ljust(1) + "\t")
            self._output_txt_file_img_frame_WE2_green.write("\n")
        self._output_txt_file_img_frame_WE2_green.close()

        for row in self._output_data_img_frame_WE2_red:
            for item in row:
                self._output_txt_file_img_frame_WE2_red.write(item.ljust(1) + "\t")
            self._output_txt_file_img_frame_WE2_red.write("\n")
        self._output_txt_file_img_frame_WE2_red.close()

        for row in self._output_data_img_frame_WE1_WE2_green:
            for item in row:
                self._output_txt_file_img_frame_WE1_WE2_green.write(item.ljust(1) + "\t")
            self._output_txt_file_img_frame_WE1_WE2_green.write("\n")
        self._output_txt_file_img_frame_WE1_WE2_green.close()

        for row in self._output_data_img_frame_WE1_WE2_red:
            for item in row:
                self._output_txt_file_img_frame_WE1_WE2_red.write(item.ljust(1) + "\t")
            self._output_txt_file_img_frame_WE1_WE2_red.write("\n")
        self._output_txt_file_img_frame_WE1_WE2_red.close()

        # WHITE
        for row in self._output_data_white_WE1_green:
            for item in row:
                self._output_txt_file_white_WE1_green.write(item.ljust(1) + "\t")
            self._output_txt_file_white_WE1_green.write("\n")
        self._output_txt_file_white_WE1_green.close()

        for row in self._output_data_white_WE1_red:
            for item in row:
                self._output_txt_file_white_WE1_red.write(item.ljust(1) + "\t")
            self._output_txt_file_white_WE1_red.write("\n")
        self._output_txt_file_white_WE1_red.close()

        for row in self._output_data_white_WE2_green:
            for item in row:
                self._output_txt_file_white_WE2_green.write(item.ljust(1) + "\t")
            self._output_txt_file_white_WE2_green.write("\n")
        self._output_txt_file_white_WE2_green.close()

        for row in self._output_data_white_WE2_red:
            for item in row:
                self._output_txt_file_white_WE2_red.write(item.ljust(1) + "\t")
            self._output_txt_file_white_WE2_red.write("\n")
        self._output_txt_file_white_WE2_red.close()

        # WHITE PRE
        for row in self._output_data_white_pre_WE1_green:
            for item in row:
                self._output_txt_file_white_pre_WE1_green.write(item.ljust(1) + "\t")
            self._output_txt_file_white_pre_WE1_green.write("\n")
        self._output_txt_file_white_pre_WE1_green.close()

        for row in self._output_data_white_pre_WE1_red:
            for item in row:
                self._output_txt_file_white_pre_WE1_red.write(item.ljust(1) + "\t")
            self._output_txt_file_white_pre_WE1_red.write("\n")
        self._output_txt_file_white_pre_WE1_red.close()

        for row in self._output_data_white_pre_WE2_green:
            for item in row:
                self._output_txt_file_white_pre_WE2_green.write(item.ljust(1) + "\t")
            self._output_txt_file_white_pre_WE2_green.write("\n")
        self._output_txt_file_white_pre_WE2_green.close()

        for row in self._output_data_white_pre_WE2_red:
            for item in row:
                self._output_txt_file_white_pre_WE2_red.write(item.ljust(1) + "\t")
            self._output_txt_file_white_pre_WE2_red.write("\n")
        self._output_txt_file_white_pre_WE2_red.close()

        # RESUME
        for row in self._output_data_resume_WE1:
            for item in row:
                self._output_txt_file_resume_WE1.write(item.ljust(1) + "\t")
            self._output_txt_file_resume_WE1.write("\n")
        self._output_txt_file_resume_WE1.close()

        for row in self._output_data_resume_WE2:
            for item in row:
                self._output_txt_file_resume_WE2.write(item.ljust(1) + "\t")
            self._output_txt_file_resume_WE2.write("\n")
        self._output_txt_file_resume_WE2.close()

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
        
        # M. Petieau - Modifying D. Verdonck's original task to apply new design with green and red frames
        Xsign = pygame.image.load(self._current_dir + 'not_available.jpg').convert()
        Xsign_rect = Xsign.get_rect(centerx=self._size[0]*0.5, centery=self._size[1]*0.78)
        Vsign = pygame.image.load(self._current_dir + 'available.jpg').convert()
        Vsign_rect = Vsign.get_rect(centerx=self._size[0]*0.5, centery=self._size[1]*0.78)
        
        run = True
        while run:
            if self._WE is True and self._count_WE1 < len(self._seq_WE1):
                self.white_screen()
                self.consigne_img_WE1()
                self.on_event(self._consigne_timer)
                self.white_screen()
                self._resume = []
                self._resume_count = 0
                for self._resume_count in range(0, 10, 1): # BLOC 10 IMG WE1
                    
                    self.match_img_WE1(self._frame_seq[self._count_WE1]) # img display + add in self._resume if necessary
                    start_img = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                    self.on_event(self._img_timer)
                    
                    self.white_screen()   # Pre white
                    stop_img_start_pre_white = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                    self.on_event(self.random_sleep())   # Sleep + allow to exit with keyboard
                    
                    self.match_img_WE1(0)   # IMG + green or red frame display here under
                    if self._frame_seq[self._count_WE1] == 1:
                        pygame.draw.rect(self._screen, (0, 255, 0), ((self._screen.get_width()/2)-425, (self._screen.get_height()/2)-300, 850, 600), 20)
                        self._screen.blit(Vsign, Vsign_rect)
                    else:
                        pygame.draw.rect(self._screen, (255, 0, 0), ((self._screen.get_width()/2)-425, (self._screen.get_height()/2)-300, 850, 600), 20)
                        self._screen.blit(Xsign, Xsign_rect)
                    pygame.display.update()
                    stop_pre_white_start_img_frame = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                    self.on_event(self._img_frame_timer)
                    
                    self.white_screen()   # white screen before next img
                    stop_img_frame_start_white = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                    self.on_event(self.random_sleep())
                    stop_white = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                    
                    if self._frame_seq[self._count_WE1] == 1:
                        self._output_data_white_WE1_green.append([str(stop_img_frame_start_white), str(stop_white-stop_img_frame_start_white), str(self._val)]) # TIMER OUTPUT WHITE SCREEN WE1 GREEN
                        self._output_data_img_noFrame_WE1_green.append([str(start_img), str(stop_img_start_pre_white-start_img), str(self._val)]) # TIMER OUTPUT IMG NOFRAME WE1 GREEN
                        self._output_data_img_noFrame_WE1_WE2_green.append([str(start_img), str(stop_img_start_pre_white-start_img), str(self._val)])
                        self._output_data_white_pre_WE1_green.append([str(stop_img_start_pre_white), str(stop_pre_white_start_img_frame-stop_img_start_pre_white), str(self._val)])
                        self._output_data_img_frame_WE1_green.append([str(stop_pre_white_start_img_frame), str(stop_img_frame_start_white-stop_pre_white_start_img_frame), str(self._val)])   # TIMER OUTPUT IMG FRAME WE1 GREEN
                        self._output_data_img_frame_WE1_WE2_green.append([str(stop_pre_white_start_img_frame), str(stop_img_frame_start_white-stop_pre_white_start_img_frame), str(self._val)])
                    else:
                        self._output_data_white_WE1_red.append([str(stop_img_frame_start_white), str(stop_white-stop_img_frame_start_white), str(self._val)]) # TIMER OUTPUT WHITE SCREEN WE1 RED
                        self._output_data_img_noFrame_WE1_red.append([str(start_img), str(stop_img_start_pre_white-start_img), str(self._val)]) # TIMER OUTPUT IMG NOFRAME WE1 RED
                        self._output_data_img_noFrame_WE1_WE2_red.append([str(start_img), str(stop_img_start_pre_white-start_img), str(self._val)])
                        self._output_data_white_pre_WE1_red.append([str(stop_img_start_pre_white), str(stop_pre_white_start_img_frame-stop_img_start_pre_white), str(self._val)])
                        self._output_data_img_frame_WE1_red.append([str(stop_pre_white_start_img_frame), str(stop_img_frame_start_white-stop_pre_white_start_img_frame), str(self._val)])   # TIMER OUTPUT IMG FRAME WE1 RED
                        self._output_data_img_frame_WE1_WE2_red.append([str(stop_pre_white_start_img_frame), str(stop_img_frame_start_white-stop_pre_white_start_img_frame), str(self._val)])
                    
                    self._count_WE1 += 1
                    
                    if self._resume_count == 9:
                        self.resume()
                        start_resume = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                        self.on_event(self._resume_timer)
                        self.white_screen()
                        stop_resume_start_baseline = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                        self._output_data_resume_WE1.append([str(start_resume), str(stop_resume_start_baseline-start_resume), str(self._val)]) # TIMER OUTPUT RESUME WE1
                
                self._WE = False
                self.on_event(self._end_timer)
                stop_baseLine = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                self._output_data_baseline.append([str(stop_resume_start_baseline), str(stop_baseLine-stop_resume_start_baseline), str(self._val)]) # TIMER OUTPUT BASELINE
            
            elif self._WE is False and self._count_WE2 < len(self._seq_WE2):
                self.white_screen()
                self.consigne_img_WE2() #SHOW IMG
                self.on_event(self._consigne_timer)
                self.white_screen()
                self._resume = []
                self._resume_count = 0
                for self._resume_count in range(0, 10, 1): # BLOC 10 IMG WE2
                    
                    self.match_img_WE2(self._frame_seq[self._count_WE2])   # img display + add in self._resume if necessary
                    start_img = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                    self.on_event(self._img_timer)
                    
                    self.white_screen()   # Pre white
                    stop_img_start_pre_white = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                    self.on_event(self.random_sleep())   # Sleep + allow to exit with keyboard
                    
                    self.match_img_WE2(0)   # IMG + green or red frame display here under
                    if self._frame_seq[self._count_WE2] == 1:
                        pygame.draw.rect(self._screen, (0, 255, 0), ((self._screen.get_width()/2)-425, (self._screen.get_height()/2)-300, 850, 600), 20)
                        self._screen.blit(Vsign, Vsign_rect)
                    else:
                        pygame.draw.rect(self._screen, (255, 0, 0), ((self._screen.get_width()/2)-425, (self._screen.get_height()/2)-300, 850, 600), 20)
                        self._screen.blit(Xsign, Xsign_rect)
                    pygame.display.update()
                    stop_pre_white_start_img_frame = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                    self.on_event(self._img_frame_timer)

                    self.white_screen()   # white screen before next img
                    stop_img_frame_start_white = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                    self.on_event(self.random_sleep())
                    stop_white = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                    
                    if self._frame_seq[self._count_WE2] == 1:
                        self._output_data_white_WE2_green.append([str(stop_img_frame_start_white), str(stop_white-stop_img_frame_start_white), str(self._val)]) # TIMER OUTPUT WHITE SCREEN WE2 GREEN
                        self._output_data_img_noFrame_WE2_green.append([str(start_img), str(stop_img_start_pre_white-start_img), str(self._val)]) # TIMER OUTPUT IMG NOFRAME WE2 GREEN
                        self._output_data_img_noFrame_WE1_WE2_green.append([str(start_img), str(stop_img_start_pre_white-start_img), str(self._val)])
                        self._output_data_white_pre_WE2_green.append([str(stop_img_start_pre_white), str(stop_pre_white_start_img_frame-stop_img_start_pre_white), str(self._val)])
                        self._output_data_img_frame_WE2_green.append([str(stop_pre_white_start_img_frame), str(stop_img_frame_start_white-stop_pre_white_start_img_frame), str(self._val)])   # TIMER OUTPUT IMG FRAME WE2 GREEN
                        self._output_data_img_frame_WE1_WE2_green.append([str(stop_pre_white_start_img_frame), str(stop_img_frame_start_white-stop_pre_white_start_img_frame), str(self._val)])
                    else:
                        self._output_data_white_WE2_red.append([str(stop_img_frame_start_white), str(stop_white-stop_img_frame_start_white), str(self._val)]) # TIMER OUTPUT WHITE SCREEN WE2 RED
                        self._output_data_img_noFrame_WE2_red.append([str(start_img), str(stop_img_start_pre_white-start_img), str(self._val)]) # TIMER OUTPUT IMG NOFRAME WE2 RED
                        self._output_data_img_noFrame_WE1_WE2_red.append([str(start_img), str(stop_img_start_pre_white-start_img), str(self._val)])
                        self._output_data_white_pre_WE2_red.append([str(stop_img_start_pre_white), str(stop_pre_white_start_img_frame-stop_img_start_pre_white), str(self._val)])
                        self._output_data_img_frame_WE2_red.append([str(stop_pre_white_start_img_frame), str(stop_img_frame_start_white-stop_pre_white_start_img_frame), str(self._val)])   # TIMER OUTPUT IMG FRAME WE2 RED
                        self._output_data_img_frame_WE1_WE2_red.append([str(stop_pre_white_start_img_frame), str(stop_img_frame_start_white-stop_pre_white_start_img_frame), str(self._val)])
                    
                    self._count_WE2 += 1
                    
                    if self._resume_count == 9:
                        self.resume()
                        start_resume = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                        self.on_event(self._resume_timer)
                        self.white_screen()
                        stop_resume_start_baseline = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                        self._output_data_resume_WE2.append([str(start_resume), str(stop_resume_start_baseline-start_resume), str(self._val)]) # TIMER OUTPUT RESUME WE2
                
                self._WE = True
                self.on_event(self._end_timer)
                stop_baseLine = (pygame.time.get_ticks()-self._clock_time_zero)/1000.0
                self._output_data_baseline.append([str(stop_resume_start_baseline), str(stop_baseLine-stop_resume_start_baseline), str(self._val)]) # TIMER OUTPUT BASELINE

            elif self._count_WE1 == len(self._seq_WE1) and self._count_WE2 == len(self._seq_WE2):
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
        #print tdata
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
