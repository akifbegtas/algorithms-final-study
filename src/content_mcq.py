# -*- coding: utf-8 -*-
# 30 çoktan seçmeli soru. correct = doğru şıkkın index'i (0=A,1=B,2=C,3=D)

MCQ = [
 # --- L1 OMNeT++ ---
 {"topic":"L1 · OMNeT++","q":"Discrete Event Simulation (DES) neyi modeller?",
  "options":["Sürekli değişen fiziksel süreçleri","Değişikliklerin belirli zaman noktalarında (olaylarda) olduğu sistemleri","Sadece matematiksel denklemleri","Yalnızca donanım devrelerini"],
  "correct":1,"explain":"DES, durumun yalnızca ayrık olaylarda (paket varışı, hasta gelişi vb.) değiştiği sistemleri modeller. Sürekli süreçler için continuous simulation gerekir."},
 {"topic":"L1 · OMNeT++","q":"OMNeT++'ta modüller birbirleriyle nasıl haberleşir?",
  "options":["Paylaşılan global değişkenlerle","Mesaj geçişi (message passing) ile","Dosya okuyarak","Doğrudan fonksiyon çağrısıyla"],
  "correct":1,"explain":"OMNeT++ bir DES framework'üdür; sistem modüllerle modellenir ve modüller mesaj geçişi (message passing) yoluyla iletişir."},
 {"topic":"L1 · OMNeT++","q":"Bir OMNeT++ projesinde modülün DAVRANIŞINI hangi dosya tanımlar?",
  "options":[".ned dosyası",".ini dosyası",".cc / .h (C++) dosyaları",".msg dosyası"],
  "correct":2,"explain":".ned yapıyı (ağ/kapı/bağlantı), .ini yapılandırmayı, .cc/.h ise modül davranışını (initialize, handleMessage) tanımlar."},

 # --- L2 OMNeT++ Part 3 ---
 {"topic":"L2 · OMNeT++","q":"OMNeT++'ta `EV` makrosu ne işe yarar?",
  "options":["Mesaj gönderir","Simülasyon log penceresine çıktı yazar (loglama)","Yeni modül oluşturur","Parametre okur"],
  "correct":1,"explain":"EV, OMNeT++'ın loglama akışıdır; cout gibi `EV << ...` ile modülün ne yaptığını log penceresine yazdırır."},
 {"topic":"L2 · OMNeT++","q":"TicToc'ta counter durum değişkeni sıfıra ulaşınca ne yapılır?",
  "options":["counter tekrar 10 yapılır","Mesaj silinir (delete msg) ve akış durur","Yeni modül eklenir","Mesaj iki kez gönderilir"],
  "correct":1,"explain":"counter initialize()'da 10'a ayarlanır, handleMessage()'da azaltılır; 0 olunca `delete msg` ile mesaj silinir, olay üretilmez ve simülasyon durur."},

 # --- L3 OMNeT++ Part 4 ---
 {"topic":"L3 · OMNeT++","q":"`check_and_cast<TicTocMsg*>(msg)` neden çıplak cast yerine tercih edilir?",
  "options":["Daha hızlı olduğu için","Dönüşüm başarısızsa sessizce nullptr döndürdüğü için","Dönüşüm başarısızsa anlaşılır bir hata fırlattığı için","Belleği otomatik temizlediği için"],
  "correct":2,"explain":"check_and_cast içeride dynamic_cast dener; tür yanlışsa sessizce nullptr vermek yerine açık bir hata fırlatır, böylece hatayı erken yakalarsın."},
 {"topic":"L3 · OMNeT++","q":"`finish()` fonksiyonu ne zaman çağrılır?",
  "options":["Her mesaj geldiğinde","Simülasyon başında","Simülasyon bittiğinde (istatistik kaydı için)","Modül oluşturulurken"],
  "correct":2,"explain":"finish() simülasyon sona erince otomatik çağrılır; genelde recordScalar() ile özet istatistikleri kaydetmek için kullanılır."},

 # --- L4 Greedy ---
 {"topic":"L4 · Greedy","q":"Greedy (açgözlü) method temelde nasıl çalışır?",
  "options":["Tüm olası çözümleri dener","Her adımda yerel (locally) optimal seçimi yapar","Problemi bağımsız alt problemlere böler","Geriye dönük tüm seçimleri geri alır"],
  "correct":1,"explain":"Greedy her adımda o an en iyi görünen (locally optimal) seçeneği alır ve global optimuma ulaşmayı umar; optimizasyon problemlerinde kullanılır."},
 {"topic":"L4 · Greedy","q":"Bir problemin kısıtını (constraint) sağlayan çözümlere ne denir?",
  "options":["Optimal solution","Feasible solution","Brute-force solution","Infeasible solution"],
  "correct":1,"explain":"Kısıtı sağlayan her çözüm 'feasible' (uygun) çözümdür. Bunların arasından en iyisi ise 'optimal' çözümdür."},
 {"topic":"L4 · Greedy","q":"Aşağıdakilerden hangisi greedy ile optimal çözülür?",
  "options":["0/1 Knapsack","Fractional Knapsack","Tüm NP-complete problemler","Hiçbiri"],
  "correct":1,"explain":"Fractional Knapsack, value/weight oranına göre greedy ile optimal çözülür. 0/1 Knapsack'te greedy başarısız olur; DP gerekir."},
 # --- L5 Big O ---
 {"topic":"L5 · Big O","q":"`O(n² + n)` ifadesi neye sadeleşir?",
  "options":["O(n)","O(n²)","O(n³)","O(2n²)"],
  "correct":1,"explain":"Big O'da yalnızca en yüksek dereceli terim tutulur: O(n²+n) → O(n²)."},
 {"topic":"L5 · Big O","q":"Floyd-Warshall algoritmasının Big O zaman karmaşıklığı nedir?",
  "options":["O(V + E)","O(V·E)","O(V³)","O(E log V)"],
  "correct":2,"explain":"Floyd-Warshall tüm düğüm çiftleri için üçlü iç içe döngü kullanır → O(V³). (BFS/DFS O(V+E), Bellman-Ford O(VE).)"},
 {"topic":"L5 · Big O","q":"Big O sadeleştirmesinde aşağıdakilerden hangisi DOĞRUDUR?",
  "options":["Sabit katsayılar korunur","En düşük dereceli terim tutulur","Sabitler atılır ve en yüksek dereceli terim tutulur","Tüm terimler toplanır"],
  "correct":2,"explain":"Big O'da sabit katsayılar atılır (O(2n)→O(n)) ve sadece en yüksek dereceli terim tutulur (O(n²+n)→O(n²))."},

 # --- L6 ---
 {"topic":"L6 · T(n)","q":"`for(i=0;i<n;i++) for(j=0;j<n;j++) x++;` kodunun T(n) karmaşıklığı nedir?",
  "options":["O(n)","O(n²)","O(log n)","O(n³)"],
  "correct":1,"explain":"İç içe iki döngü, her biri n kez → n×n = O(n²). İç içe döngülerde karmaşıklıklar çarpılır."},
 {"topic":"L6 · T(n)","q":"`for(i=n; i>1; i=i/2) x++;` döngüsünün karmaşıklığı nedir?",
  "options":["O(n)","O(n²)","O(log n)","O(1)"],
  "correct":2,"explain":"i her adımda yarıya iner (n→n/2→...→1), yaklaşık log₂n adım. Yarıya bölme → O(log n)."},

 # --- L7 ---
 {"topic":"L7 · Pandas","q":"Pandas'ta null (boş) içeren satırları silmek için hangi metot kullanılır?",
  "options":["fillna()","dropna()","drop_duplicates()","head()"],
  "correct":1,"explain":"dropna() null içeren satırları kaldırır. fillna() boşlukları bir değerle doldurur, drop_duplicates() duplike satırları siler."},
 {"topic":"L7 · Matplotlib","q":"Matplotlib'te noktaları çizgiyle bağlamadan, dağılım grafiği çizen fonksiyon hangisidir?",
  "options":["plot()","bar()","scatter()","pie()"],
  "correct":2,"explain":"scatter() her gözlem için bağımsız bir nokta çizer (dağılım). plot() varsayılan olarak noktaları çizgiyle bağlar."},

 # --- L8 ---
 {"topic":"L8 · Dijkstra","q":"Dijkstra algoritması hangi koşulda DOĞRU çalışmaz?",
  "options":["Yönlü grafiklerde","Negatif ağırlıklı kenarlar olduğunda","Çok sayıda düğüm olduğunda","Yönsüz grafiklerde"],
  "correct":1,"explain":"Dijkstra greedy'dir; ziyaret edilen düğümü kesinleştirir. Negatif kenarlar sonradan daha kısa yol yaratabileceği için yanlış sonuç verir."},
 {"topic":"L8 · Dijkstra","q":"Dijkstra hangi algoritma paradigmasını kullanır?",
  "options":["Divide and conquer","Dynamic programming","Greedy","Backtracking"],
  "correct":2,"explain":"Dijkstra greedy'dir: her adımda ziyaret edilmemiş en küçük mesafeli düğümü seçer ve kesinleştirir."},
 {"topic":"L8 · Dijkstra","q":"Dijkstra'da 'relaxation' koşulu aşağıdakilerden hangisidir?",
  "options":["if d[u] > d[v] + w(u,v)","if d[v] > d[u] + w(u,v) then d[v]=d[u]+w(u,v)","if d[v] == d[u]","if w(u,v) < 0"],
  "correct":1,"explain":"Relaxation: u üzerinden v'ye yol daha kısaysa güncelle → if d[v] > d[u]+w(u,v) then d[v]=d[u]+w(u,v)."},

 # --- L9 ---
 {"topic":"L9 · Bellman-Ford","q":"Bellman-Ford algoritmasının zaman karmaşıklığı nedir?",
  "options":["O(V²)","O(V·E)","O(E log V)","O(V + E)"],
  "correct":1,"explain":"Bellman-Ford V-1 tur döner, her turda E kenarı gevşetir → O(V·E)."},
 {"topic":"L9 · Bellman-Ford","q":"Bellman-Ford'un Dijkstra'ya göre temel avantajı nedir?",
  "options":["Daha hızlıdır","Negatif ağırlıklı kenarları işleyebilir ve negatif çevrim tespit eder","Daha az bellek kullanır","Sadece ağaçlarda çalışır"],
  "correct":1,"explain":"Bellman-Ford negatif kenarlarla çalışır ve negatif çevrim tespit eder; bedeli daha yüksek O(VE) zamanıdır."},

 # --- L10 ---
 {"topic":"L10 · MST","q":"V düğümlü bir grafın minimum spanning tree'sinde kaç kenar bulunur?",
  "options":["V","V−1","V+1","E−1"],
  "correct":1,"explain":"Bir spanning tree tüm V düğümü çevrimsiz bağlar; bir ağaçta tam olarak V−1 kenar vardır."},
 {"topic":"L10 · MST","q":"Kruskal algoritmasında çevrim (cycle) tespiti için hangi yapı kullanılır?",
  "options":["Priority queue","Union-Find (Disjoint Set)","Hash table","Stack"],
  "correct":1,"explain":"Kruskal, bir kenarın iki ucu aynı kümede mi diye Union-Find ile bakar; aynı kümedeyse kenar çevrim oluşturur ve atlanır."},
 {"topic":"L10 · MST","q":"Prim ve Kruskal algoritmaları hangi paradigmaya dayanır?",
  "options":["Dynamic programming","Greedy","Backtracking","Divide and conquer"],
  "correct":1,"explain":"Hem Prim hem Kruskal greedy'dir; her adımda yerel en iyi (en ucuz) kenarı seçerek MST kurarlar."},

 # --- L11 ---
 {"topic":"L11 · BFS/DFS","q":"BFS (Breadth-First Search) hangi veri yapısını kullanır?",
  "options":["Stack","Queue","Priority queue","Heap"],
  "correct":1,"explain":"BFS queue (FIFO) kullanır ve grafı seviye seviye gezer. DFS ise stack/recursion kullanır."},
 {"topic":"L11 · BFS/DFS","q":"BFS ve DFS'in zaman karmaşıklığı nedir?",
  "options":["O(V·E)","O(V²)","O(V + E)","O(E log V)"],
  "correct":2,"explain":"Her düğüm bir kez, her kenar bir kez işlenir → O(V+E). Her kenara yalnızca bir kez bakıldığı için O(V·E) değildir."},

 # --- L12 ---
 {"topic":"L12 · Knapsack","q":"Fractional Knapsack problemi optimal olarak hangi yöntemle çözülür?",
  "options":["Dynamic programming","Greedy (value/weight oranına göre)","Backtracking","BFS"],
  "correct":1,"explain":"Nesneler bölünebildiği için value/weight oranına göre azalan sırayla almak (greedy) optimaldir."},
 {"topic":"L12 · Knapsack","q":"0/1 Knapsack için aşağıdakilerden hangisi DOĞRUDUR?",
  "options":["Greedy her zaman optimal sonucu verir","Nesneler bölünebilir","Dynamic programming ile O(n·W) çözülür","Sadece negatif değerlerle çalışır"],
  "correct":2,"explain":"0/1'de nesne bölünemez ve greedy başarısız olabilir; DP ile O(n·W) zamanda optimal çözülür."},

 # --- L13 ---
 {"topic":"L13 · Topological Sort","q":"Kahn algoritması bir grafikte çevrim (cycle) olduğunu nasıl anlar?",
  "options":["Kenar sayısı V'den fazlaysa","Sonuç listesinin boyutu düğüm sayısına (V) eşit değilse","Tüm in-degree'ler 0 ise","Queue başta boşsa"],
  "correct":1,"explain":"Çevrimdeki düğümlerin in-degree'si hiç 0 olmaz, kuyruğa girmezler. Sonuçta result.size() != V ise çevrim vardır."},
]

print("MCQ loaded:", len(MCQ))
