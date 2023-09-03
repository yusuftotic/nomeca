from os import system
from time import sleep
from random import randint, choice

menu_main = """
Hoşgeldiniz.

[0] İşlemler
[1] Sayılar
[2] Günler ve Aylar
[Q] Çıkış
"""

# İŞLEMLER
menu_operations = """
Hoşgeldiniz.

[0] Toplama
[1] Çıkarma
[2] Çarpma
[3] Bölme
[Q] Çıkış
"""

# TOPLAMA MENÜLERİ
menu_addition = """
Toplama İşlemine Hoşgeldiniz.

[0] Toplama İşlemi Öğren
[1] Toplama İşlemi İle İlgili Alıştırmalar
[Q] Geri
"""

menu_additionLearning = """
En Fazla İki Basamaklı Olan İki Sayı Değeri Girin.
[Q] Geri
"""

menu_additionExamples = """
Verilen İki Sayıyı Toplayın ve Sonucu Yazın.
[Q] Geri
"""

# ÇIKARMA MENÜLERİ
menu_subtraction = """
Çıkarma İşlemine Hoşgeldiniz.

[0] Çıkarma İşlemi Öğren
[1] Çıkarma İşlemi İle İlgili Alıştırmalar
[Q] Geri
"""

menu_subtractionLearning = """
En Fazla İki Basamaklı Olan İki Sayı Değeri Girin.
[Q] Geri
"""

menu_subtractionExamples = """
Verilen İki Sayıyı Çıkarın ve Sonucu Yazın.
[Q] Geri
"""

# ÇARPMA MENÜLERİ
menu_multiplication = """
Çarpma İşlemine Hoşgeldiniz.

[0] Çarpma İşlemi Öğren
[1] Çarpma İşlemi İle İlgili Alıştırmalar
[Q] Geri
"""

menu_multiplicationLearning = """
En Fazla İki Basamaklı Olan İki Sayı Değeri Girin.
[Q] Geri
"""

menu_multiplicationExamples = """
Verilen İki Sayıyı Çarpın ve Sonucu Yazın.
[Q] Geri
"""

# BÖLME MENÜLERİ
menu_division = """
Bölme İşlemine Hoşgeldiniz.

[0] Bölme İşlemi Öğren
[1] Bölme İşlemi İle İlgili Alıştırmalar
[Q] Geri
"""

menu_divisionLearning = """
En Fazla İki Basamaklı Olan İki Sayı Değeri Girin.
[Q] Geri
"""

menu_divisionExamples = """
Verilen İki Sayıyı Bölün ve Sonucu Yazın.
[Q] Geri
"""
#################################################################
menu_numbers = """
Verilen Sayıyı Harfle Yazın.
[Q] Geri
"""
#################################################################
menu_daysMonths = """
Hoşgeldiniz.

[1] Günler
[2] Aylar
[Q] Ana Menüye Dön
"""

day_menu = """
[1] Haftanın günleri öğren
[2] Haftanın günleriyle alıştırmalar yap
[Q] Ana Menü
"""

months_menu = """
[1] Ayları öğren
[2] Aylarla ilgili alıştırmalar
[Q] Ana Menü
"""


day_menuExamples ="""
Haftanın günleriyle alıştırmalar yap
[Q]Geri
"""

months_menuExamples = """
Aylarla alıştırma yap
[Q]Geri
"""


def getMenu(menu):
    
    system("cls")

    # Ana menü
    if menu == "daysMonths":
        print(menu_daysMonths)

    # Günler menüsü
    elif menu == "day":
        print(day_menu)

    elif menu == "dayExamples":
        print(day_menuExamples)

    # Aylar menüsü
    elif menu == "months":
        print(months_menu)
    elif menu == "monthExamples":
        print(months_menuExamples)

# ANA MENÜ
    elif menu == 'operations':
        print(menu_operations)

    # TOPLAMA MENÜSÜ
    elif menu == 'addition':
        print(menu_addition)

    # TOPLAMA ÖĞRENME MENÜSÜ
    elif menu == 'additionLearning':
        print(menu_additionLearning)
    
    # TOPLAMA İLE İLGİLİ ALIŞTIRMALAR MENÜSÜ
    elif menu == 'additionExamples':
        print(menu_additionExamples)

    # ÇIKARMA MENÜSÜ
    elif menu == 'subtraction':
        print(menu_subtraction)

    # ÇIKARMA ÖĞRENME MENÜSÜ
    elif menu == 'subtractionLearning':
        print(menu_subtractionLearning)
    
    # ÇIKARMA İLE İLGİLİ ALIŞTIRMALAR MENÜSÜ
    elif menu == 'subtractionExamples':
        print(menu_subtractionExamples)

    # ÇARPMA MENÜSÜ
    elif menu == 'multiplication':
        print(menu_multiplication)

    # ÇARPMA ÖĞRENME MENÜSÜ
    elif menu == 'multiplicationLearning':
        print(menu_multiplicationLearning)
    
    # ÇARPMA İLE İLGİLİ ALIŞTIRMALAR MENÜSÜ
    elif menu == 'multiplicationExamples':
        print(menu_multiplicationExamples)

    # BÖLME MENÜSÜ
    elif menu == 'division':
        print(menu_division)

    # BÖLME ÖĞRENME MENÜSÜ
    elif menu == 'divisionLearning':
        print(menu_divisionLearning)
    
    # BÖLME İLE İLGİLİ ALIŞTIRMALAR MENÜSÜ
    elif menu == 'divisionExamples':
        print(menu_divisionExamples)
    # Ana Menü
    elif menu == 'menu_numbers':
        print(menu_numbers)

while True:

    system('cls')

    print(menu_main)

    menuChoice_main = str(input("\nHangisiyle devam etmek istersiniz? : "))

    # İŞLEMLER
    if menuChoice_main == '0':
        ## FUNCTIONS

        def getInt(value):

            return str(value).split('.')[0]

        def getDecimal(value):

            return str(value).split('.')[1]


        # MAIN LOOP
        while True:

            getMenu('operations')
            
            menuChoice_operations = str(input('Alıştırma Yapmak İstediğiniz İşlemi Seçiniz: '))
            
        ############################################################################################################################

            ## TOPLAMA İŞLEMİ
            if menuChoice_operations == '0':

                while True:

                    getMenu('addition')

                    menuChoice_addition = str(input('Hangisiyle Devam Etmek İstersiniz ?: '))

                    # TOPLAMA İŞLEMİ ÖĞREN
                    if menuChoice_addition == '0':
                        
                        while True:

                            getMenu('additionLearning')

                            # Toplama Öğren - Kullanıcı İlk Sayıyı Girer
                            firstNumber_additionLearning = input('İlk Sayıyı Girin: ')

                            # Toplama Öğren - İlk Sayının Üçten Az Basamaklı ve Boş Karakter Olup Olmadığı Kontrol Edilir, Üç veya Üçten Fazla Basamaklıysa Döngünün Başına Gidilir
                            if len(str(firstNumber_additionLearning)) >= 3 or len(str(firstNumber_additionLearning)) == 0:
                                print('\nSayı En Fazla İki Basamaklı Olmalı! Tekrar Deneyin.')
                                sleep(1.5)
                                continue
                            
                            # Toplama Öğren - İlk Inputta Kullanıcının Çıkış Yapma İsteği Değerlendirilir
                            elif firstNumber_additionLearning == 'Q' or firstNumber_additionLearning == 'q':

                                system('cls')
                                print('Bir Önceki Menüye Gidililiyor...')
                                sleep(1.5)
                                break

                            # Toplama Öğren - Kullanıcı İkinci Sayıyı Girer
                            secondNumber_additionLearning = input('\nİkinci Sayıyı Girin: ')

                            # Toplama Öğren - İkinci Sayının Üçten Az Basamaklı Olup Olmadığı Kontrol Edilir, Üç veya Üçten Fazla Basamaklıysa Döngünün Başına Gidilir
                            if len(str(secondNumber_additionLearning)) >= 3 or len(str(secondNumber_additionLearning)) == 0:
                                print('\nSayı En Fazla İki Basamaklı Olmalı! Tekrar Deneyin.')
                                sleep(1.5)
                                continue

                            # Toplama Öğren - İkinci Inputta Kullanıcının Geri Dönme İsteği Değerlendirilir
                            elif secondNumber_additionLearning == 'Q' or secondNumber_additionLearning == 'q':
                                
                                system('cls')
                                print('Bir Önceki Menüye Gidiliyor...')
                                sleep(1.5)
                                break

                            # Toplama Öğren - Kullanıcının Girdiği İki Sayının Toplamı Bulunur
                            result_additionLearning = int(firstNumber_additionLearning) + int(secondNumber_additionLearning)

                            # Toplama Öğren - Kullanıcının Girdiği İki Sayının Toplamı Ekrana Yazadırılır
                            print(f'\n{firstNumber_additionLearning} + {secondNumber_additionLearning} = {result_additionLearning}')
                            sleep(1.5)
                            continue

                    # TOPLAMA İŞLEMİ İLE İLGİLİ ALIŞTIRMALAR
                    elif menuChoice_addition == '1':

                        while True:

                            # Toplama Alıştırmaları Menüsü Fonksiyon ile Çağırılır
                            getMenu('additionExamples')

                            try:

                                # Toplama Alıştırmaları - Birinci Sayı Random Olarak Oluşturulur
                                firstNumber_additionExamples = randint(0, 99)

                                # Toplama Alıştırmaları - İkinci Sayı Random Olarak Oluşturulur
                                secondNumber_additionExamples = randint(0, 99)

                                # Toplama Alıştırmaları - İki Sayının Toplamı Sistem Tarafından Bulunur: Doğru Cevap
                                result_additionExamples = firstNumber_additionExamples + secondNumber_additionExamples
                                    
                                # Toplama Alıştırmaları - Sorunun Cevabının Üçten Az Basamaklı Olup Olmadığı Kontrol Edilir, Üç veya Üçten Fazla Basamaklıysa Döngünün Başına Gidilir
                                if len(str(result_additionExamples)) >= 3:
                                    continue
                                        
                                # Toplama Alıştırmaları - Kullanıcıdan Cevap Alınır
                                input_additionExamples = input(f'\n{firstNumber_additionExamples} + {secondNumber_additionExamples} = ').strip()

                                # Toplama Alıştırmaları - Q ile Bir Önceki Menüye Döner
                                if input_additionExamples == 'Q' or input_additionExamples == 'q':

                                    system('cls')
                                    print('Bir Önceki Menüye Gidiliyor...')
                                    sleep(1.5)
                                    break

                                # Toplama Alıştırmaları - Cevap Doğru ise
                                elif int(input_additionExamples) == result_additionExamples:
                                        
                                    print(f'\nAferin {input_additionExamples} Doğru Cevap!')
                                    sleep(1.5)
                                    continue

                                # Toplama Alıştırmaları - Cevap Yanlış ise
                                elif int(input_additionExamples) != result_additionExamples:
                                        
                                    # print('\nMaalesef {} Yanlış Cevap!'.format(input_additionExamples))
                                    print(f'\nMaalesef {input_additionExamples} Yanlış Cevap!')
                                    sleep(1.5)
                                    continue

                            # Toplama Alıştırmaları - ValueError Hatası Alınırsa Burada Yakalanır
                            except ValueError:

                                # Toplama Alıştırmaları - Yakalanan Hata Kullanıcıya Bildirilir
                                print('\nGeçersiz Cevap! Tekrar Deneyin.')
                                sleep(1.5)
                                continue

                    # GERİ
                    elif menuChoice_addition == 'Q' or menuChoice_addition == 'q':
                        system('cls')
                        print('Bir Önceki Menüye Gidiliyor...')
                        sleep(1.5)
                        break

                    else:
                        print('\nGeçersiz Seçim! Tekrar Deneyin.\n')
                        sleep(1.5)
                        continue

        ############################################################################################################################
            
            ## ÇIKARMA İŞLEMİ
            elif menuChoice_operations == '1':
                
                while True:

                    getMenu('subtraction')

                    menuChoice_subtraction = str(input('Hangisiyle Devam Etmek İstersiniz: '))

                    # ÇIKARMA İŞLEMİ ÖĞREN
                    if menuChoice_subtraction == '0':
                        
                        while True:

                            getMenu('subtractionLearning')

                            # Çıkarma Öğren - Kullanıcı İlk Sayıyı Girer
                            firstNumber_subtractionLearning = input('Eksilen Sayıyı Girin: ')

                            # Çıkarma Öğren - İlk Sayının Üçten Az Basamaklı Olup Olmadığı Kontrol Edilir, Üç veya Üçten Fazla Basamaklıysa Döngünün Başına Gidilir
                            if len(str(firstNumber_subtractionLearning)) >= 3 or len(str(firstNumber_subtractionLearning)) == 0:
                                print('\nSayı En Fazla İki Basamaklı Olmalı! Tekrar Deneyin.')
                                sleep(1.5)
                                continue
                            
                            # Çıkarma Öğren - İlk Inputta Kullanıcının Çıkış Yapma İsteği Değerlendirilir
                            elif firstNumber_subtractionLearning == 'Q' or firstNumber_subtractionLearning == 'q':

                                system('cls')
                                print('Bir Önceki Menüye Gidiliyor...')
                                sleep(1.5)
                                break

                            # Çıkarma Öğren - Kullanıcı İkinci Sayıyı Girer
                            secondNumber_subtractionLearning = input('\nÇıkan Sayıyı Girin: ')

                            # Çıkarma Öğren - İkinci Sayının Üçten Az Basamaklı Olup Olmadığı Kontrol Edilir, Üç veya Üçten Fazla Basamaklıysa Döngünün Başına Gidilir
                            if len(str(secondNumber_subtractionLearning)) >= 3 or len(str(secondNumber_subtractionLearning)) == 0:
                                print('\nSayı En Fazla İki Basamaklı Olmalı! Tekrar Deneyin.')
                                sleep(1.5)
                                continue

                            # Çıkarma Öğren - İkinci Inputta Kullanıcının Geri Dönme İsteği Değerlendirilir
                            elif secondNumber_subtractionLearning == 'Q' or secondNumber_subtractionLearning == 'q':
                                
                                system('cls')
                                print('Bir Önceki Menüye Gidiliyor...')
                                sleep(1.5)
                                break

                            # Çıkarma Öğren - Eksilen Sayı, Çıkan Sayıdan Küçük ise
                            if int(firstNumber_subtractionLearning) < int(secondNumber_subtractionLearning):

                                print('\nÇıkan Sayı, Eksilen Sayıdan Büyük Olamaz!')
                                sleep(1.5)
                                continue

                            # Çıkarma Öğren - Eksilen Sayı, Çıkan Sayıdan Büyük veya Eşit ise
                            elif int(firstNumber_subtractionLearning) >= int(secondNumber_subtractionLearning):

                                # Çıkarma Öğren - Kullanıcının Girdiği İki Sayının Farkı Bulunur
                                result_subtractionLearning = int(firstNumber_subtractionLearning) - int(secondNumber_subtractionLearning)

                            # Çıkarma Öğren - Kullanıcının Girdiği İki Sayının Farkı Ekrana Yazadırılır
                            print(f'\n{firstNumber_subtractionLearning} - {secondNumber_subtractionLearning} = {result_subtractionLearning}')
                            sleep(1.5)
                            continue

                    # ÇIKARMA İŞLEMİ İLE İLGİLİ ALIŞTIRMALAR
                    elif menuChoice_subtraction == '1':

                        while True:

                            # Çıkarma Alıştırmaları Menüsü Fonksiyon ile Çağırılır
                            getMenu('subtractionExamples')

                            try:

                                # Çıkarma Alıştırmaları - Birinci Sayı Random Olarak Oluşturulur
                                firstNumber_subtractionExamples = randint(0, 99)

                                # Çıkarma Alıştırmaları - İkinci Sayı Random Olarak Oluşturulur
                                secondNumber_subtractionExamples = randint(0, 99)
                                
                                # Çıkarma Alıştırmaları - Eksilen ve Çıkan Kontrolü
                                if firstNumber_subtractionExamples < secondNumber_subtractionExamples:
                                    continue

                                # Çıkarma Alıştırmaları - İki Sayının Farkı Sistem Tarafından Bulunur: Doğru Cevap
                                result_subtractionExamples = firstNumber_subtractionExamples - secondNumber_subtractionExamples
                                    
                                # Çıkarma Alıştırmaları - Sorunun Cevabının Üçten Az Basamaklı Olup Olmadığı Kontrol Edilir, Üç veya Üçten Fazla Basamaklıysa Döngünün Başına Gidilir
                                if len(str(result_subtractionExamples)) >= 3:
                                    continue

                                # Çıkarma Alıştırmaları - Kullanıcıdan Cevap Alınır
                                input_subtractionExamples = input(f'\n{firstNumber_subtractionExamples} - {secondNumber_subtractionExamples} = ').strip()

                                # Çıkarma Alıştırmaları - Q ile Bir Önceki Menüye Döner
                                if input_subtractionExamples == 'Q' or input_subtractionExamples == 'q':

                                    system('cls')
                                    print('Bir Önceki Menüye Gidiliyor...')
                                    sleep(1.5)
                                    break

                                # Çıkarma Alıştırmaları - Cevap Doğru ise
                                elif int(input_subtractionExamples) == result_subtractionExamples:
                                        
                                    print(f'\nAferin {input_subtractionExamples} Doğru Cevap!')
                                    sleep(1.5)
                                    continue

                                # Çıkarma Alıştırmaları - Cevap Yanlış ise
                                elif int(input_subtractionExamples) != result_subtractionExamples:
                                        
                                    print(f'\nMaalesef {input_subtractionExamples} Yanlış Cevap!')
                                    sleep(1.5)
                                    continue

                            # Çıkarma Alıştırmaları - ValueError Hatası Alınırsa Burada Yakalanır
                            except ValueError:

                                # Çıkarma Alıştırmaları - Yakalanan Hata Kullanıcıya Bildirilir
                                print('\nGeçersiz Cevap! Tekrar Deneyin.')
                                sleep(1.5)
                                continue

                    # GERİ
                    elif menuChoice_subtraction == 'Q' or menuChoice_subtraction == 'q':
                        system('cls')
                        print('Bir Önceki Menüye Gidiliyor...')
                        sleep(1.5)
                        break

                    else:
                        print('\nGeçersiz Seçim! Tekrar Deneyin.\n')
                        sleep(1.5)
                        continue
            
        ############################################################################################################################

            ## ÇARPMA İŞLEMİ
            elif menuChoice_operations == '2':

                while True:

                    getMenu('multiplication')

                    menuChoice_multiplication = str(input('Hangisiyle Devam Etmek İstersiniz: '))

                    # ÇARPMA İŞLEMİ ÖĞREN
                    if menuChoice_multiplication == '0':
                        
                        while True:

                            getMenu('multiplicationLearning')

                            # Çarpma Öğren - Kullanıcı İlk Sayıyı Girer
                            firstNumber_multiplicationLearning = input('İlk Sayıyı Girin: ')

                            # Çarpma Öğren - İlk Sayının Üçten Az Basamaklı Olup Olmadığı Kontrol Edilir, Üç veya Üçten Fazla Basamaklıysa Döngünün Başına Gidilir
                            if len(str(firstNumber_multiplicationLearning)) >= 3 or len(str(firstNumber_multiplicationLearning)) == 0:
                                print('\nSayı En Fazla İki Basamaklı Olmalı! Tekrar Deneyin.')
                                sleep(1.5)
                                continue
                            
                            # Çarpma Öğren - İlk Inputta Kullanıcının Çıkış Yapma İsteği Değerlendirilir
                            elif firstNumber_multiplicationLearning == 'Q' or firstNumber_multiplicationLearning == 'q':

                                system('cls')
                                print('Bir Önceki Menüye Gidiliyor...')
                                sleep(1.5)
                                break

                            # Çarpma Öğren - Kullanıcı İkinci Sayıyı Girer
                            secondNumber_multiplicationLearning = input('\nİkinci Sayıyı Girin: ')

                            # Çarpma Öğren - İkinci Sayının Üçten Az Basamaklı Olup Olmadığı Kontrol Edilir, Üç veya Üçten Fazla Basamaklıysa Döngünün Başına Gidilir
                            if len(str(secondNumber_multiplicationLearning)) >= 3 or len(str(secondNumber_multiplicationLearning)) == 0:
                                print('\nSayı En Fazla İki Basamaklı Olmalı! Tekrar Deneyin.')
                                sleep(1.5)
                                continue

                            # Çarpma Öğren - İkinci Inputta Kullanıcının Geri Dönme İsteği Değerlendirilir
                            elif secondNumber_multiplicationLearning == 'Q' or secondNumber_multiplicationLearning == 'q':
                                
                                system('cls')
                                print('Bir Önceki Menüye Gidiliyor...')
                                sleep(1.5)
                                break

                            # Çarpma Öğren - Kullanıcının Girdiği İki Sayının Çarpımı Bulunur
                            result_multiplicationLearning = int(firstNumber_multiplicationLearning) * int(secondNumber_multiplicationLearning)

                            # Çarpma Öğren - Kullanıcının Girdiği İki Sayının Çarpımı Ekrana Yazadırılır
                            print(f'\n{firstNumber_multiplicationLearning} x {secondNumber_multiplicationLearning} = {result_multiplicationLearning}')
                            sleep(1.5)
                            continue

                    # ÇARPMA İŞLEMİ İLE İLGİLİ ALIŞTIRMALAR
                    elif menuChoice_multiplication == '1':

                        while True:

                            # Çarpma Alıştırmaları Menüsü Fonksiyon ile Çağırılır
                            getMenu('multiplicationExamples')

                            try:

                                # Çarpma Alıştırmaları - Birinci Sayı Random Olarak Oluşturulur
                                firstNumber_multiplicationExamples = randint(0, 10)

                                # Çarpma Alıştırmaları - İkinci Sayı Random Olarak Oluşturulur
                                secondNumber_multiplicationExamples = randint(0, 10)

                                # Çarpma Alıştırmaları - İki Sayının Çarpımı Sistem Tarafından Bulunur: Doğru Cevap
                                result_multiplicationExamples = firstNumber_multiplicationExamples * secondNumber_multiplicationExamples
                                    
                                # Çarpma Alıştırmaları - Sorunun Cevabının Üçten Az Basamaklı Olup Olmadığı Kontrol Edilir, Üç veya Üçten Fazla Basamaklıysa Döngünün Başına Gidilir
                                if len(str(result_multiplicationExamples)) >= 3:
                                    continue
                                        
                                # Çarpma Alıştırmaları - Kullanıcıdan Cevap Alınır
                                input_multiplicationExamples = input(f'\n{firstNumber_multiplicationExamples} x {secondNumber_multiplicationExamples} = ').strip()

                                # Çarpma Alıştırmaları - Q ile Bir Önceki Menüye Döner
                                if input_multiplicationExamples == 'Q' or input_multiplicationExamples == 'q':

                                    system('cls')
                                    print('Bir Önceki Menüye Gidiliyor...')
                                    sleep(1.5)
                                    break

                                # Çarpma Alıştırmaları - Cevap Doğru ise
                                elif int(input_multiplicationExamples) == result_multiplicationExamples:
                                        
                                    print(f'\nAferin {input_multiplicationExamples} Doğru Cevap!')
                                    sleep(1.5)
                                    continue

                                # Çarpma Alıştırmaları - Cevap Yanlış ise
                                elif int(input_multiplicationExamples) != result_multiplicationExamples:
                                        
                                    print(f'\nMaalesef {input_multiplicationExamples} Yanlış Cevap!')
                                    sleep(1.5)
                                    continue

                            # Çarpma Alıştırmaları - ValueError Hatası Alınırsa Burada Yakalanır
                            except ValueError:

                                # Çarpma Alıştırmaları - Yakalanan Hata Kullanıcıya Bildirilir
                                print('\nGeçersiz Cevap! Tekrar Deneyin.')
                                sleep(1.5)
                                continue

                    # GERİ
                    elif menuChoice_multiplication == 'Q' or menuChoice_multiplication == 'q':
                        system('cls')
                        print('Bir Önceki Menüye Gidiliyor...')
                        sleep(1.5)
                        break

                    else:
                        print('\nGeçersiz Seçim! Tekrar Deneyin.\n')
                        sleep(1.5)
                        continue

        ############################################################################################################################
            
            ## BÖLME İŞLEMİ
            elif menuChoice_operations == '3':
                
                while True:

                    getMenu('division')

                    menuChoice_division = str(input('Hangisiyle Devam Etmek İstersiniz: '))

                    # BÖLME İŞLEMİ ÖĞREN
                    if menuChoice_division == '0':
                        
                        while True:

                            getMenu('divisionLearning')

                            firstNumber_divisionLearning = str(input('\nİlk Sayı: '))
                            # basamak kontrolü
                            if len(str(firstNumber_divisionLearning)) >= 3 or len(str(firstNumber_divisionLearning)) == 0:
                                print('\nSayı en fazla 2 basamaklı olmalı!')
                                sleep(1.5)
                                continue
                            #çıkış
                            if firstNumber_divisionLearning == 'Q' or firstNumber_divisionLearning == 'q':
                                system('cls')
                                print('\nÇıkış yapılıyor...')
                                sleep(1.5)
                                break


                            secondNumber_divisionLearning = str(input('\nİkinci Sayı: '))            
                            # basamak kontrolü
                            if len(str(secondNumber_divisionLearning)) >= 3 or len(str(secondNumber_divisionLearning)) == 0:
                                print('\nSayı en fazla 2 basamaklı olmalı!')
                                sleep(1.5)
                                continue
                            # İkinci sayı 0 olamaz
                            if int(secondNumber_divisionLearning) == 0:
                                print('\nİkinci sayı 0 olamaz')
                                sleep(1.5)
                                continue
                            #çıkış
                            if secondNumber_divisionLearning == 'Q' or secondNumber_divisionLearning == 'q':
                                system('cls')
                                print('\nÇıkış yapılıyor...')
                                sleep(1.5)
                                break

                            # büyüklük kontrolü
                            if int(firstNumber_divisionLearning) < int(secondNumber_divisionLearning):
                                print('\nÇıkan sayı büyük olmaz')
                                sleep(1.5)
                                continue

                            result_divisionLearning = int(firstNumber_divisionLearning) / int(secondNumber_divisionLearning)

                            if getDecimal(result_divisionLearning) != '0':
                                print('\nTam bölünmez!')
                                sleep(1.5)
                                continue

                            print(f'\n{firstNumber_divisionLearning} : {secondNumber_divisionLearning} = {getInt(result_divisionLearning)}')

                            sleep(1.5)

                    # BÖLME İŞLEMİ İLE İLGİLİ ALIŞTIRMALAR
                    elif menuChoice_division == '1':

                        while True:

                            # Bölme Alıştırmaları Menüsü Fonksiyon ile Çağırılır
                            getMenu('divisionExamples')

                            firstNumber_divisionExamples = randint(0, 99)
                            # basamak kontrolü
                            if len(str(firstNumber_divisionExamples)) >= 3 or len(str(firstNumber_divisionExamples)) == 0:
                                continue

                            secondNumber_divisionExamples = randint(2, 99)

                            # aynı olmasınlar
                            

                            # basamak kontrolü
                            if len(str(secondNumber_divisionExamples)) >= 3 or len(str(secondNumber_divisionExamples)) == 0:
                                continue

                            # büyüklük kontrolü
                            if int(firstNumber_divisionExamples) < int(secondNumber_divisionExamples):
                                continue

                            result_divisionExamples = int(firstNumber_divisionExamples) / int(secondNumber_divisionExamples)

                            #float kontrol
                            if getDecimal(result_divisionExamples) != '0':
                                getMenu('divisionExamples')
                                continue

                            input_divisionExamples = str(input(f'\n{firstNumber_divisionExamples} : {secondNumber_divisionExamples} = '))
                            #çıkış
                            if input_divisionExamples == 'Q' or input_divisionExamples == 'q':
                                system('cls')
                                print('\nÇıkış yapılıyor...')
                                sleep(1.5)
                                break

                            elif int(getInt(result_divisionExamples)) == int(input_divisionExamples):
                                print(f'\n{input_divisionExamples} Doğru')
                                sleep(1.5)
                                continue

                            elif int(getInt(result_divisionExamples)) != int(input_divisionExamples):
                                print(f'\n{input_divisionExamples} Yanlış')
                                sleep(1.5)
                                continue

                    # GERİ
                    elif menuChoice_division == 'Q' or menuChoice_division == 'q':
                        system('cls')
                        print('Bir Önceki Menüye Gidiliyor...')
                        sleep(1.5)
                        break

                    else:
                        print('\nGeçersiz Seçim! Tekrar Deneyin.\n')
                        sleep(1.5)
                        continue

        ############################################################################################################################

            ## ÇIKIŞ İŞLEMİ
            elif menuChoice_operations == 'Q' or menuChoice_operations == 'q':
                system('cls')
                print('Ana menüye dönülüyor...')
                sleep(1.5)
                break

        ############################################################################################################################

            ## GEÇERSİZ GİRİŞ
            else:
                print('\nGeçersiz Seçim! Tekrar Deneyin.')
                sleep(1.5)
                continue


    # SAYILAR
    if menuChoice_main == '1':

        def cevir(x):
            birlik_sayi=int(x%10)
            onluk_sayi=int(x/10)
            if birlik_sayi!=0:
                if birlik_sayi==1:
                    birlik_yazi="bir"
                if birlik_sayi==2:
                    birlik_yazi="iki"
                if birlik_sayi==3:
                    birlik_yazi="üç"
                if birlik_sayi==4:
                    birlik_yazi="dört"
                if birlik_sayi==5:
                    birlik_yazi="beş"
                if birlik_sayi==6:
                    birlik_yazi="altı"
                if birlik_sayi==7:
                    birlik_yazi="yedi"
                if birlik_sayi==8:
                    birlik_yazi="sekiz"
                if birlik_sayi==9:
                    birlik_yazi="dokuz"

            if x>9:
                if onluk_sayi==1:
                    onluk_yazi="on"
                if onluk_sayi==2:
                    onluk_yazi="yirmi"
                if onluk_sayi==3:
                    onluk_yazi="otuz"
                if onluk_sayi==4:
                    onluk_yazi="kırk"
                if onluk_sayi==5:
                    onluk_yazi="elli"
                if onluk_sayi==6:
                    onluk_yazi="altmış"
                if onluk_sayi==7:
                    onluk_yazi="yetmiş"
                if onluk_sayi==8:
                    onluk_yazi="seksen"
                if onluk_sayi==9:
                    onluk_yazi="doksan"
            return onluk_yazi+" "+birlik_yazi

        while True:
            
            getMenu('menu_numbers')
        
    
            try:
                

                system('cls')
                

                sayi = randint(1, 100)

                dogruCevap = cevir(sayi)

                cevap = str(input(f'{sayi} yazı ile yazın: ')).lower()

                if cevap == dogruCevap:
                    print('\nBildin.')
                    sleep(1.5)
                    continue

                elif str(cevap) == 'q' or str(cevap) == 'Q':
                    system('cls')
                    print('\nAna menüye dönülüyor')
                    sleep(1)
                    break
                
                else:
                    print('\nBilemedin')
                    sleep(1.5)

            except UnboundLocalError:
                continue


    # GÜNLER VE AYLAR
    if menuChoice_main == '2':

        while True:

            getMenu("daysMonths")

            choiseMenu_main = str(input("Lütfen çalışmak istediğiniz konuyu seçiniz : "))

            if choiseMenu_main == "1":

                while True:
                    getMenu("day")

                    choiseMenu_day =str(input("Lütfen yapmak istediğiniz işlemi seçiniz : "))

                    if choiseMenu_day == "1":
                        print("1.Gün: Pazartesi", "2.Gün: Salı", "3.Gün: Çarşamba", "4:Gün: Perşembe", "5.Gün: Cuma", "6.Gün: Cumartesi", "7.Gün: Pazar" ,sep= "\n")
                        sleep(5)
                        pass
                    elif choiseMenu_day == "2":

                        while True:
                            getMenu("dayExamples") 
                            days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
                            day = choice(days)
                            input_answer = input(f'\n{day} haftanın kaçıncı günüdür? : ')

                            

                            # Pazartesi
                            if day == days[0]:
                                answer = '1'

                            # Salı
                            elif day == days[1]:
                                answer = '2'

                            # Çarşamba
                            elif day == days[2]:
                                answer = '3'

                            # Perşembe
                            elif day == days[3]:
                                answer = '4'

                            # Cuma
                            elif day == days[4]:
                                answer = '5'

                            # Cumartesi
                            elif day == days[5]:
                                answer = '6'

                            # Pazar
                            elif day == days[6]:
                                answer = '7'

                            if input_answer == "q" or input_answer == "Q":
                                print("Günler menüsüne dönülüyor")
                                sleep(1.5)
                                break

                            if str(answer) == str(input_answer):
                                print('\nDoğru Cevap!')
                                sleep(1.5)
                                continue

                            elif str(answer) != str(input_answer):
                                print('\nYanlış Cevap!')
                                sleep(1.5)
                                continue

                    elif choiseMenu_day == "q" or choiseMenu_day == "Q":
                        print("Ana menüye dönülüyor")
                        sleep(1.5)
                        break

            elif choiseMenu_main == "2":

                while True:
                    getMenu("months")

                    choiseMenu_months = str(input("Lütfen çalışmak istediğiniz konuyu seçiniz : ")) 
                    if choiseMenu_months == "1" :
                        print("1.Ay: Ocak", "2.Ay: Şubat", "3.Ay: Mart", "4:Ay: Nisan", "5.Ay: Mayıs", "6.Ay: Haziran", "7.Ay: Temmuz","8.Ay: Ağustos","9.Ay: Eylül","10.Ay: Ekim","11.Ay: Kasım", "12.Ay: Ağustos" ,sep= "\n")
                        sleep(5)
                        pass
                    elif choiseMenu_months == "2":

                        while True:                   
                            getMenu("monthExamples")
                            months = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
                            month = choice(months)
                            input_answer = input(f'\n{month} yılın kaçıncı ayıdır? : ')

                            #Ocak
                            if month == months[0]:
                                answer = '1'
                        #Şubat
                            elif month == months[1]:
                                answer = '2' 
                            #Mart
                            elif month == months[2]:
                                answer = '3'
                            #Nisan
                            elif month == months[3]:
                                answer = '4'
                            #Mayıs
                            elif month == months[4]:
                                answer = '5'
                        #Haziran
                            elif month == months[5]:
                                answer = '6'
                            #Temmuz
                            elif month == months[6]:
                                answer = '7'
                        #Ağustos
                            elif month == months[7]:
                                answer = '8'
                        #Eylül
                            elif month == months[8]:
                                answer = '9'
                            #Ekim
                            elif month == months[9]:
                                answer = '10'
                            #Kasım
                            elif month == months[10]:
                                answer = '11'
                        #Aralık
                            elif month == months[11]:
                                answer = '12'
                            
                            if input_answer == "q" or input_answer == "Q":
                                print("Aylar menüsüne dönülüyor")
                                sleep(1.5)
                                break
                            if str(answer) == str(input_answer):
                                print('\nDoğru Cevap!')
                                sleep(1.5)
                                continue

                            elif str(answer) != str(input_answer):
                                print('\nYanlış Cevap!')
                                sleep(1.5)
                                continue
                    elif choiseMenu_months == "q" or choiseMenu_months == "Q":
                        print("Ana menüye dönülüyor")
                        sleep(1.5)
                        break
                                
            elif choiseMenu_main == 'Q' or choiseMenu_main == 'q':
                print("Çıkış Yapılıyor!")
                sleep(1.5)
                break


    # ÇIKIŞ
    if menuChoice_main == 'Q' or menuChoice_main == 'q':
        pass