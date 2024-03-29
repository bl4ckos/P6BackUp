# ======================================================================================================================
# TITLE           : Sauvegarde site web sur site distant
# DESCRIPTION     :
# - Sauvegarde de la bases de donnée présente sur le serveur
# - Sauvegarde de la bases de donnée sur serveur distant
# AUTHORS         : ASSELINO MARVIN
# DATE            : 02/09/2018
#https://github.com/bl4ckos
# ========================================================================================================================
#!/usr/bin/python3                                                          # mon script sera version 3 du langage python 

import shutil, tarfile, time, datetime, os, subprocess, sys, yaml           # j'import de la bibliothéque les modules suivant qui permet d'utiliser des définitions et instructions
import datetime as dt
from itertools import chain


jobType = sys.argv[1]           # jobtype détermine l'execution du script sauvegarde ou restore  sys.argv 1 lance grace a l'import sys argument 1
confFile = sys.argv[2]          # confFile fichier de config contient mes variables 

############### Functions Definitions ######################      c"est une suite d'instructions que l'on peut appeler avec un nom 
def readConf(file): #lecture du fichier de conf 
  with open(file, 'r') as stream: # ouvrir le fichier file/conf et le lire comme repertoire courant
    try:                           # essayer dans un premier bloc une instruction et en 2eme bloc instruction en cas d'erreur 
      return yaml.safe_load(stream) # renvoyer la conf yaml safe load convertis un fichier yaml en python 
    except yaml.YAMLError as exc: # erreur d'execution du fichier yaml
      print(exc)                    # montre moi l'execution 
##### specifique restore #####
def get_BkpFile(aday): #calcul du nom d'un fichier de sauvegarde selon son jour
    ago = dt.datetime.now() - dt.timedelta(days=aday) # je calcule le delta entre today et une date anterieur ( on remonte de x jours)
    date = ago.strftime("%Y%m%d")   # je traduis la date du jour avec strftime Année mois et jour collé (dans le format que j'ai besoin)
    bkpfile = "backup" + date + ".tar"    # bkpfile sera nommé backup avec la date du jour et le .tar pour la compression
    return bkpfile     # renvois le fichier bkpfile je sais pas comment l'expliquer 

def getNextract(file): #scp et extraction du fichier de sauvegarde
    print("restore du fichier" + file)        # montre moi  le fichier file 
    proc = subprocess.Popen(['scp', Vars['restore']['user'] + '@' + Vars['restore']['ip'] + ':~/' + file, '.']) # process scp qui permet de transferer le fichier .tar vars = va au fichier yaml lire les instructions 'user' 'ip'
    time.sleep(5)       # met un temps de 5 secondes entre chaque execution pour qu'il laisse le temps de transferer le fichier .tar
    try:                # essayer 
        tar = tarfile.open(file)   # ouvrir le fichier tar 
        tar.extractall()            # extraire l'integralité du fichier
        tar.close()                 # fermer l'execution du programme tar
    except tarfile.ExtractError as e:       # si une error me retourner comme indication erreur de niveau 2
        raise errorlevel == 2

##### specifique save #####
def checkDiskSpace(): #verification de l'espace disk
  try:   # essayer
    total, used, free = shutil.disk_usage("/")   # lister l'espace de stockage total utilisé et libre 
    return free                                  # renvoyer l'espace libre
  except OSError as err:                         # code erreur 
    if err.args[0] != errno.ENOENT:                 # si 
      raise                         # lever une exception
    else:                           # sinon si
      self.fail("OSError not raised")  # 

def getBackupFileName(): #calculer le nom du fichier de sauvegarde d'aujourd'hui (
  timestr = time.strftime("%Y%m%d")   #traduction de la date 
  return "backup" + timestr + ".tar"   # on retourne le nom du fichier
                    

def createBackup(file): #creation de la sauvegarde
  try:  #essayer
    tar = tarfile.open(Vars['save']['dir'] + file,"w")  # w = ecriture
  except tarfile.CompressionError as e:   # erreur de compression 
    raise CRCError(e)
  now = dt.datetime.now()     
  ago = now - dt.timedelta(days=1)   # ago = maintenant - days 1  (calculer la date d'hier)
    for root, dirs, files in chain.from_iterable(os.walk(path) for path in Vars['save']['paths']): # dans nos listes de dossier nous les prenons un par un ( os.walk lire le contenu du dossier path ) on le découpe en dossier et fichier 
    for fname in files:   # fname le chemin des fichier ( pour chaque fichier dans la liste des fichiers ) 
      path = os.path.join(root, fname)    # joindre le chemin en root 
      if dt.datetime.weekday(now) == 6:    # si la date du jour est 6 = dimanche 
        tar.add(path)                       # ajoute le fichier a la sauvegarde  
      else:                                 # sinon
        st = os.stat(path)                  # recuperer les statistiques du fichier
        mtime = dt.datetime.fromtimestamp(st.st_mtime)  # on récupére la date de modification du fichier
        if mtime > ago:                     #si la date du fichier est supérieur à la date d'hier 
        tar.add(path)                       # ajouter les fichiers 

def exportBackup(file): #export de la sauvegarde
  try:
  proc = subprocess.Popen(['scp', Vars['save']['dir'] + file, Vars['save']['user'] + '@' + Vars['save']['ip'] + ':~/'])
  except BaseException as e:
        logging.error(str(e))
        logging.error('Problème au niveau de la connexion SCP!!')
  # transfert du fichier 
###### fonction save() = prog principal du script save ######
def save():
  if checkDiskSpace() >= 1000:  # si disque est supérieur ou égal à 1gb 
    print("test ok")            # dit moi test ok 
  else:                         # sinon
    print("espace indisponible") # dit moi espace indisponible 
    exit(1)
  
  tarFile = getBackupFileName()
  createBackup(tarFile)
  exportBackup(tarFile)

    
###### fonction restore() = prog principal du script restore ######
def restore():
  now = dt.datetime.now()           # now = la commande datetime now 
  day = dt.datetime.weekday(now)    # day est égal à maintenant 
  sunday = day+1                    # dimanche est égal à jour +1 
  sunday_bkpfile = get_BkpFile(sunday)  # le fichier de dimanche 
  getNextract(sunday_bkpfile)           # restore le fichier de dimanche 
  for i in range(day, 0, -1):           # dans l'ordre dimanche jusqu'au jour le plus recent
    daily_bkpfile = get_BkpFile(i)      # on restore le fichier du jour de dimanche au jour le plus recent
    getNextract(daily_bkpfile)          # extract chaque jour 
    

########### main code ###########
Vars = readConf(confFile)           # conf de lancement si jobtype lance sauvegarde sinon lance restore 
print(jobType)
if jobType == 'save':
  save()
elif jobType == 'restore':
  restore()
else:
  print('va bosser')
