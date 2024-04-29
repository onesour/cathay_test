## 程式邏輯題目
第一~三題分別為logic_01.py、logic_02.py、logic_03.py。  
分別運行以下command即可測試。
```shell
python logic_01.py
python logic_02.py
python logic_03.py
```

## 自動化測試
採用pytest框架撰寫，測試程式碼在test_cathay.py。

appium環境設置可參考以下兩篇文章。
* https://coolpaidasin.gitbooks.io/mobile_automation/content/ru-he-you-python-script-qidong-android-mo-ni-qi.html
* https://appium.io/docs/en/latest/quickstart/install/  

運行測試時請先下載python相依套件。
```shell
pip install -r requirements.txt
```
測試程式請直接在專案底下運行pytest，pytest相依的opts已寫在pytest.ini中。
```shell
pytest
```
