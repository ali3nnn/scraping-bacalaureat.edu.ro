# This code has been used in Google Colab at the following url https://colab.research.google.com/drive/1O1nyRzF-xLMn9fcYVycHAM1Ad0_rY2WO?usp=sharing

# Cell 1
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# Cell 2
# !pip install selenium
# !apt-get update # to update ubuntu to correctly run apt install
# !apt install chromium-chromedriver
# !cp /usr/lib/chromium-browser/chromedriver /usr/bin

# Cell 3
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

# Cell 4
dataEdu = { }

# Cell 5
def getData(rows_1, rows_2, dataEdu):
    for row_1 in rows_1:
      # print('row_1', len(row_1.find_all()))
      if len(row_1.find_all()) == 21:
        pozitie_clasament = row_1.find_all('td',{"class":"tdBac"})[0].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[0].contents) else 'lipsa pozitie'
        cod = row_1.find_all('td',{"class":"tdBac"})[1].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[1].contents) else 'lipsa cod'
        unitatea = row_1.find_all('td',{"class":"tdBac"})[2].find_all('a')[0].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[2].contents) else 'lipsa unitate'
        judet = row_1.find_all('td',{"class":"tdBac"})[3].find_all('a')[0].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[3].contents) else 'lipsa judet'
        promotie_anterioara = row_1.find_all('td',{"class":"tdBac"})[4].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[4].contents) else 'lipsa promotie'
        forma_de_invatamant = row_1.find_all('td',{"class":"tdBac"})[5].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[5].contents) else 'lipsa forma de inv'
        profil = row_1.find_all('td',{"class":"tdBac"})[6].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[6].contents) else 'lipsa profil'
        oral_lb_romana = row_1.find_all('td',{"class":"tdBac"})[7].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[7].contents) else 'lipsa oral lb rom'
        scris_lb_romana_initial = row_1.find_all('td',{"class":"tdBac"})[8].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[8].contents) else 'lipsa scris lb rom'
        scris_lb_romana_contestatie = row_1.find_all('td',{"class":"tdBac"})[9].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[9].contents) else 'lipsa scris lb rom'
        scris_lb_romana_final = row_1.find_all('td',{"class":"tdBac"})[10].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[10].contents) else 'lipsa scris lb rom'
        limba_moderna = row_1.find_all('td',{"class":"tdBac"})[12].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[12].contents) else 'lipsa lb moderna'
        calificativ_limba_moderna = row_1.find_all('td',{"class":"tdBac"})[13].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[13].contents) else 'lipsa calif lb moderna'
        disciplina_profilului = row_1.find_all('td',{"class":"tdBac"})[14].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[14].contents) else 'lipsa disciplina profilului'
        disciplina_optionala = row_1.find_all('td',{"class":"tdBac"})[15].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[15].contents) else 'lipsa disciplina optionala'
        competente_digitale = row_1.find_all('td',{"class":"tdBac"})[16].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[16].contents) else 'lipsa compentente digitale'
        media = row_1.find_all('td',{"class":"tdBac"})[17].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[17].contents) else 'lipsa media'
        rezultatul_final = row_1.find_all('td',{"class":"tdBac"})[18].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[18].contents) else 'lipsa rez final'

        print(pozitie_clasament, cod)
        # if pozitie_clasament > 2090:

        if 'pozitie_clasament' in dataEdu:  
          dataEdu['pozitie_clasament'].append(pozitie_clasament)
        else:
          dataEdu['pozitie_clasament'] = [pozitie_clasament]
        if 'cod' in dataEdu:
          dataEdu['cod'].append(cod)
        else:
          dataEdu['cod'] = [cod]
        if 'unitatea' in dataEdu:
          dataEdu['unitatea'].append(unitatea)
        else:
          dataEdu['unitatea'] = [unitatea]
        if 'judet' in dataEdu:
          dataEdu['judet'].append(judet)
        else:
          dataEdu['judet'] = [judet]
        if 'promotie_anterioara' in dataEdu:
          dataEdu['promotie_anterioara'].append(promotie_anterioara)
        else:
          dataEdu['promotie_anterioara'] = [promotie_anterioara]
        if 'forma_de_invatamant' in dataEdu:
          dataEdu['forma_de_invatamant'].append(forma_de_invatamant)
        else:
          dataEdu['forma_de_invatamant'] = [forma_de_invatamant]
        if 'profil' in dataEdu:
          dataEdu['profil'].append(profil)
        else:
          dataEdu['profil'] = [profil]
        if 'oral_lb_romana' in dataEdu:
          dataEdu['oral_lb_romana'].append(oral_lb_romana)
        else:
          dataEdu['oral_lb_romana'] = [oral_lb_romana]
        if 'scris_lb_romana_initial' in dataEdu:
          dataEdu['scris_lb_romana_initial'].append(scris_lb_romana_initial)
        else:
          dataEdu['scris_lb_romana_initial'] = [scris_lb_romana_initial]
        if 'scris_lb_romana_contestatie' in dataEdu:
          dataEdu['scris_lb_romana_contestatie'].append(scris_lb_romana_contestatie)
        else:
          dataEdu['scris_lb_romana_contestatie'] = [scris_lb_romana_contestatie]
        if 'scris_lb_romana_final' in dataEdu:
          dataEdu['scris_lb_romana_final'].append(scris_lb_romana_final)
        else:
          dataEdu['scris_lb_romana_final'] = [scris_lb_romana_final]
        if 'limba_moderna' in dataEdu:
          dataEdu['limba_moderna'].append(limba_moderna)
        else:
          dataEdu['limba_moderna'] = [limba_moderna]
        if 'calificativ_limba_moderna' in dataEdu:
          dataEdu['calificativ_limba_moderna'].append(calificativ_limba_moderna)
        else:
          dataEdu['calificativ_limba_moderna'] = [calificativ_limba_moderna]
        if 'disciplina_profilului' in dataEdu:
          dataEdu['disciplina_profilului'].append(disciplina_profilului)
        else:
          dataEdu['disciplina_profilului'] = [disciplina_profilului]
        if 'disciplina_optionala' in dataEdu:
          dataEdu['disciplina_optionala'].append(disciplina_optionala)
        else:
          dataEdu['disciplina_optionala'] = [disciplina_optionala]
        if 'competente_digitale' in dataEdu:
          dataEdu['competente_digitale'].append(competente_digitale)
        else:
          dataEdu['competente_digitale'] = [competente_digitale]
        if 'media' in dataEdu:
          dataEdu['media'].append(media)
        else:
          dataEdu['media'] = [media]
        if 'rezultatul_final' in dataEdu:
          dataEdu['rezultatul_final'].append(rezultatul_final)
        else:
          dataEdu['rezultatul_final'] = [rezultatul_final]
      else:
        nota_disciplina_profilului_initial = row_1.find_all('td',{"class":"tdBac"})[4].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[4].contents) else 'lipsa nota'
        nota_disciplina_profilului_contestatie = row_1.find_all('td',{"class":"tdBac"})[5].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[5].contents) else 'lipsa nota'
        nota_disciplina_profilului_final = row_1.find_all('td',{"class":"tdBac"})[6].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[6].contents) else 'lipsa nota'
        nota_disciplina_optionala_initial = row_1.find_all('td',{"class":"tdBac"})[7].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[7].contents) else 'lipsa nota'
        nota_disciplina_optionala_contestatie = row_1.find_all('td',{"class":"tdBac"})[8].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[8].contents) else 'lipsa nota'
        nota_disciplina_optionala_final = row_1.find_all('td',{"class":"tdBac"})[9].contents[0] if len(row_1.find_all('td',{"class":"tdBac"})[9].contents) else 'lipsa nota'

        if 'nota_disciplina_profilului_initial' in dataEdu:
          dataEdu['nota_disciplina_profilului_initial'].append(nota_disciplina_profilului_initial)
        else:
          dataEdu['nota_disciplina_profilului_initial'] = [nota_disciplina_profilului_initial]
        if 'nota_disciplina_profilului_contestatie' in dataEdu:
          dataEdu['nota_disciplina_profilului_contestatie'].append(nota_disciplina_profilului_contestatie)
        else:
          dataEdu['nota_disciplina_profilului_contestatie'] = [nota_disciplina_profilului_contestatie]
        if 'nota_disciplina_profilului_final' in dataEdu:
          dataEdu['nota_disciplina_profilului_final'].append(nota_disciplina_profilului_final)
        else:
          dataEdu['nota_disciplina_profilului_final'] = [nota_disciplina_profilului_final]
        if 'nota_disciplina_optionala_initial' in dataEdu:
          dataEdu['nota_disciplina_optionala_initial'].append(nota_disciplina_optionala_initial)
        else:
          dataEdu['nota_disciplina_optionala_initial'] = [nota_disciplina_optionala_initial]
        if 'nota_disciplina_optionala_contestatie' in dataEdu:
          dataEdu['nota_disciplina_optionala_contestatie'].append(nota_disciplina_optionala_contestatie)
        else:
          dataEdu['nota_disciplina_optionala_contestatie'] = [nota_disciplina_optionala_contestatie]
        if 'nota_disciplina_optionala_final' in dataEdu:
          dataEdu['nota_disciplina_optionala_final'].append(nota_disciplina_optionala_final)
        else:
          dataEdu['nota_disciplina_optionala_final'] = [nota_disciplina_optionala_final]

    for row_2 in rows_2:
      # print('row_2', len(row_2.find_all()))
      if len(row_2.find_all()) == 21:
        pozitie_clasament = row_2.find_all('td',{"class":"tdBac"})[0].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[0].contents) else 'lipsa pozitie'
        cod = row_2.find_all('td',{"class":"tdBac"})[1].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[1].contents) else 'lipsa cod'
        unitatea = row_2.find_all('td',{"class":"tdBac"})[2].find_all('a')[0].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[2].contents) else 'lipsa unitate'
        judet = row_2.find_all('td',{"class":"tdBac"})[3].find_all('a')[0].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[3].contents) else 'lipsa judet'
        promotie_anterioara = row_2.find_all('td',{"class":"tdBac"})[4].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[4].contents) else 'lipsa promotie'
        forma_de_invatamant = row_2.find_all('td',{"class":"tdBac"})[5].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[5].contents) else 'lipsa forma de inv'
        profil = row_2.find_all('td',{"class":"tdBac"})[6].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[6].contents) else 'lipsa profil'
        oral_lb_romana = row_2.find_all('td',{"class":"tdBac"})[7].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[7].contents) else 'lipsa oral lb rom'
        scris_lb_romana_initial = row_2.find_all('td',{"class":"tdBac"})[8].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[8].contents) else 'lipsa scris lb rom'
        scris_lb_romana_contestatie = row_2.find_all('td',{"class":"tdBac"})[9].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[9].contents) else 'lipsa scris lb rom'
        scris_lb_romana_final = row_2.find_all('td',{"class":"tdBac"})[10].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[10].contents) else 'lipsa scris lb rom'
        limba_moderna = row_2.find_all('td',{"class":"tdBac"})[12].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[12].contents) else 'lipsa lb moderna'
        calificativ_limba_moderna = row_2.find_all('td',{"class":"tdBac"})[13].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[13].contents) else 'lipsa calif lb moderna'
        disciplina_profilului = row_2.find_all('td',{"class":"tdBac"})[14].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[14].contents) else 'lipsa disciplina profilului'
        disciplina_optionala = row_2.find_all('td',{"class":"tdBac"})[15].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[15].contents) else 'lipsa disciplina optionala'
        competente_digitale = row_2.find_all('td',{"class":"tdBac"})[16].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[16].contents) else 'lipsa compentente digitale'
        media = row_2.find_all('td',{"class":"tdBac"})[17].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[17].contents) else 'lipsa media'
        rezultatul_final = row_2.find_all('td',{"class":"tdBac"})[18].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[18].contents) else 'lipsa rez final'

        print(pozitie_clasament, cod)

        if 'pozitie_clasament' in dataEdu:
          dataEdu['pozitie_clasament'].append(pozitie_clasament)
        else:
          dataEdu['pozitie_clasament'] = [pozitie_clasament]
        if 'cod' in dataEdu:
          dataEdu['cod'].append(cod)
        else:
          dataEdu['cod'] = [cod]
        if 'unitatea' in dataEdu:
          dataEdu['unitatea'].append(unitatea)
        else:
          dataEdu['unitatea'] = [unitatea]
        if 'judet' in dataEdu:
          dataEdu['judet'].append(judet)
        else:
          dataEdu['judet'] = [judet]
        if 'promotie_anterioara' in dataEdu:
          dataEdu['promotie_anterioara'].append(promotie_anterioara)
        else:
          dataEdu['promotie_anterioara'] = [promotie_anterioara]
        if 'forma_de_invatamant' in dataEdu:
          dataEdu['forma_de_invatamant'].append(forma_de_invatamant)
        else:
          dataEdu['forma_de_invatamant'] = [forma_de_invatamant]
        if 'profil' in dataEdu:
          dataEdu['profil'].append(profil)
        else:
          dataEdu['profil'] = [profil]
        if 'oral_lb_romana' in dataEdu:
          dataEdu['oral_lb_romana'].append(oral_lb_romana)
        else:
          dataEdu['oral_lb_romana'] = [oral_lb_romana]
        if 'scris_lb_romana_initial' in dataEdu:
          dataEdu['scris_lb_romana_initial'].append(scris_lb_romana_initial)
        else:
          dataEdu['scris_lb_romana_initial'] = [scris_lb_romana_initial]
        if 'scris_lb_romana_contestatie' in dataEdu:
          dataEdu['scris_lb_romana_contestatie'].append(scris_lb_romana_contestatie)
        else:
          dataEdu['scris_lb_romana_contestatie'] = [scris_lb_romana_contestatie]
        if 'scris_lb_romana_final' in dataEdu:
          dataEdu['scris_lb_romana_final'].append(scris_lb_romana_final)
        else:
          dataEdu['scris_lb_romana_final'] = [scris_lb_romana_final]
        if 'limba_moderna' in dataEdu:
          dataEdu['limba_moderna'].append(limba_moderna)
        else:
          dataEdu['limba_moderna'] = [limba_moderna]
        if 'calificativ_limba_moderna' in dataEdu:
          dataEdu['calificativ_limba_moderna'].append(calificativ_limba_moderna)
        else:
          dataEdu['calificativ_limba_moderna'] = [calificativ_limba_moderna]
        if 'disciplina_profilului' in dataEdu:
          dataEdu['disciplina_profilului'].append(disciplina_profilului)
        else:
          dataEdu['disciplina_profilului'] = [disciplina_profilului]
        if 'disciplina_optionala' in dataEdu:
          dataEdu['disciplina_optionala'].append(disciplina_optionala)
        else:
          dataEdu['disciplina_optionala'] = [disciplina_optionala]
        if 'competente_digitale' in dataEdu:
          dataEdu['competente_digitale'].append(competente_digitale)
        else:
          dataEdu['competente_digitale'] = [competente_digitale]
        if 'media' in dataEdu:
          dataEdu['media'].append(media)
        else:
          dataEdu['media'] = [media]
        if 'rezultatul_final' in dataEdu:
          dataEdu['rezultatul_final'].append(rezultatul_final)
        else:
          dataEdu['rezultatul_final'] = [rezultatul_final]
      else:
        nota_disciplina_profilului_initial = row_2.find_all('td',{"class":"tdBac"})[4].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[4].contents) else 'lipsa nota'
        nota_disciplina_profilului_contestatie = row_2.find_all('td',{"class":"tdBac"})[5].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[5].contents) else 'lipsa nota'
        nota_disciplina_profilului_final = row_2.find_all('td',{"class":"tdBac"})[6].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[6].contents) else 'lipsa nota'
        nota_disciplina_optionala_initial = row_2.find_all('td',{"class":"tdBac"})[7].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[7].contents) else 'lipsa nota'
        nota_disciplina_optionala_contestatie = row_2.find_all('td',{"class":"tdBac"})[8].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[8].contents) else 'lipsa nota'
        nota_disciplina_optionala_final = row_2.find_all('td',{"class":"tdBac"})[9].contents[0] if len(row_2.find_all('td',{"class":"tdBac"})[9].contents) else 'lipsa nota'

        if 'nota_disciplina_profilului_initial' in dataEdu:
          dataEdu['nota_disciplina_profilului_initial'].append(nota_disciplina_profilului_initial)
        else:
          dataEdu['nota_disciplina_profilului_initial'] = [nota_disciplina_profilului_initial]
        if 'nota_disciplina_profilului_contestatie' in dataEdu:
          dataEdu['nota_disciplina_profilului_contestatie'].append(nota_disciplina_profilului_contestatie)
        else:
          dataEdu['nota_disciplina_profilului_contestatie'] = [nota_disciplina_profilului_contestatie]
        if 'nota_disciplina_profilului_final' in dataEdu:
          dataEdu['nota_disciplina_profilului_final'].append(nota_disciplina_profilului_final)
        else:
          dataEdu['nota_disciplina_profilului_final'] = [nota_disciplina_profilului_final]
        if 'nota_disciplina_optionala_initial' in dataEdu:
          dataEdu['nota_disciplina_optionala_initial'].append(nota_disciplina_optionala_initial)
        else:
          dataEdu['nota_disciplina_optionala_initial'] = [nota_disciplina_optionala_initial]
        if 'nota_disciplina_optionala_contestatie' in dataEdu:
          dataEdu['nota_disciplina_optionala_contestatie'].append(nota_disciplina_optionala_contestatie)
        else:
          dataEdu['nota_disciplina_optionala_contestatie'] = [nota_disciplina_optionala_contestatie]
        if 'nota_disciplina_optionala_final' in dataEdu:
          dataEdu['nota_disciplina_optionala_final'].append(nota_disciplina_optionala_final)
        else:
          dataEdu['nota_disciplina_optionala_final'] = [nota_disciplina_optionala_final]

# Cell 6
wd.get("http://bacalaureat.edu.ro/Pages/TaraRezultMedie.aspx")

# try:
select = Select(wd.find_element(By.ID, "ContentPlaceHolderBody_DropDownList2"))
select.select_by_value('800')
# except:
  # print(wd.page_source)

for page in range(13000):

  # time_to_wait_between_pages = random.uniform(2, 3)
  # time.sleep(time_to_wait_between_pages)
  # print(f'Pagina {page} - wait {time_to_wait_between_pages} seconds')
  print(f'Pagina {page}')

  startPage = 0
    
  if page%10 == 0 and page>startPage and 'cod' in dataEdu.keys():
    print("randuri scanate:", len(dataEdu['cod']))
    df = pd.DataFrame(data=dataEdu)
    filename = f'dataEdu_startPage_{startPage}.csv' # because sometimes the host intrerrupts the scraping, you have to save the files in batches
    compression_opts = dict(method='zip', archive_name=filename)  
    df.to_csv(f'/content/drive/MyDrive/Work/bacStats/{filename}', index=False)  
    # time_to_wait_between_pages = random.uniform(3, 5)
    # print(f'{filename} was saved - wait {time_to_wait_between_pages} seconds')
    print(f'{filename} was saved')
    # time.sleep(time_to_wait_between_pages)

  try: 

    html = wd.page_source
    soup = BeautifulSoup(html, "html.parser")
    mainTable = soup.find_all('table', {"class":"mainTable"})[0]
    rows_1 = mainTable.find_all('tr',{"class":"tr1"})
    rows_2 = mainTable.find_all('tr',{"class":"tr2"})
    
    getData(rows_1, rows_2,dataEdu);

    # print(len(rows_1), len(rows_2))
    
    # print(len(row_1))
    # print(rows_1[0].find_all('td',{"class":"tdBac"})[1].contents[0])
    # print(cod)

    td = wd.find_element(By.ID, "ContentPlaceHolderBody_ImageButtonDR1_1")
    td.send_keys("\n")

  except Exception as e:
    print(e)
    break
    # time.sleep(10)
    # print(html)
    # wd.quit()
    # wd.get("http://bacalaureat.edu.ro/Pages/TaraRezultMedie.aspx")
    continue

# Example output from cell 6:
# Pagina 1
# 8001 SJ1223673
# 8003 SM1201969
# 8005 SV1195832
# 8007 SV1196025
# 8009 SV1204320
# 8002 SJ1262812
# 8004 SM1203548
# 8006 SV1195990
# 8008 SV1198718
# 8010 SV1204872
# Pagina 2
# 8011 SV1215258
# 8013 SV1238879
# 8015 SV1248432
# 8017 SV1278827
# 8019 SV1289594
# 8012 SV1238498
# 8014 SV1241055
# 8016 SV1273850
# 8018 SV1288365
# 8020 SV1290297
# Pagina 3
# 8021 SV1298661
# 8023 TL1205596
# 8025 TL1220643
# 8027 TL1232936
# 8029 TM1197767
# 8022 TL1205519
# 8024 TL1217322
# 8026 TL1222586
# 8028 TM1192862
# 8030 TM1207919
