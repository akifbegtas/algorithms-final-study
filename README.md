# Analysis of Algorithms — Final Çalışma Kılavuzu

C++ tabanlı **Data Structures & Analysis of Algorithms** dersi için interaktif final
çalışma kılavuzu. Tek bir `index.html` dosyasında; konu anlatımları (kod parçalarıyla),
detaylı soru-cevaplar, otomatik puanlı çoktan seçmeli sınav ve kod-boşluk-doldurmaca
klasik sorular bulunur.

## 🚀 Nasıl kullanılır
`index.html` dosyasına çift tıkla — tarayıcıda açılır. Kurulum/derleme gerekmez.

## 📚 İçindekiler
- **13 ders** (L1–L13) konu anlatımı + gömülü C++ / sözde kod
- **91 detaylı soru-cevap** (her ders için 7, tıklayınca açılan cevaplar)
- **30 soruluk çoktan seçmeli sınav** — otomatik puanlama + her soruya açıklama
- **14 klasik kod sorusu** — boşluk doldurmaca, çözümü gizli

### Konular
| Ders | Konu |
|------|------|
| L1 | C++'a giriş (namespace, switch, dizi, sınıf, constructor) |
| L2 | Veri yapıları & Bağlı listeler (Linked List, template) |
| L3 | Iteration, Induction, Recursion + Selection Sort |
| L4 | Big O, Big Ω, Big Θ — karmaşıklık analizi |
| L5 | Bubble, Insertion, Selection Sort |
| L6 | Algoritma analizi — T(n) ve toplam denklemleri |
| L7 | Pandas, DataFrame, Matplotlib |
| L8 | Dijkstra — en kısa yol |
| L9 | Bellman-Ford |
| L10 | Minimum Cost Spanning Tree (Prim & Kruskal) |
| L11 | Graf gezinmeleri — BFS & DFS |
| L12 | Knapsack (sırt çantası) problemi |
| L13 | Topolojik sıralama — Kahn algoritması |

## 🛠️ Yeniden üretme (opsiyonel)
İçerik `src/` altındaki Python dosyalarından üretilir:

```bash
cd src
python3 build.py        # -> index.html üretir
```

- `content_lectures.py` — konu anlatımı + soru-cevaplar
- `content_mcq.py` — çoktan seçmeli sorular
- `content_classic.py` — klasik kod soruları
- `build.py` — HTML derleyici (markdown render + quiz motoru)

## ⚠️ Not
Kod örnekleri standart C++ / sözde kod olarak yeniden yazılmıştır. Sınavda hocanın gösterimi
farklıysa onu esas alın. Kişisel çalışma amaçlıdır.
