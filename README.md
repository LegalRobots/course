# course

#### Hinweis für Mac User - Software Update zu Mac OS 10.12.5

Falls im Terminal beim Versuch, jupyter notebook zu starten, ein Execution Error auftritt: 

1. Tippt:

```jupyter notebook --generate-config```

2. Navigiert zum im Terminal angegebenen Speicherort der so generierten Config-Datei.

3. Öffnet die Datei im Editor und setzt ```c.NotebookApp.browser = u'chrome'```.


Quelle: (Issue auf GitHub)[https://github.com/jupyter/notebook/issues/2438]