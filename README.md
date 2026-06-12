# Analysis of Algorithms — Final Çalışma Kılavuzu

İnteraktif final çalışma kılavuzu (tek `index.html`): konu anlatımları (kod parçalarıyla),
detaylı soru-cevaplar, otomatik puanlı çoktan seçmeli sınav, kod-boşluk-doldurmaca klasik
sorular ve **iki çıkmış final sınavı** (2023-24 & 2024-25) çözümleriyle.

## 🚀 Nasıl kullanılır
`index.html` dosyasına çift tıkla — tarayıcıda açılır. Kurulum gerekmez.

## 📚 İçindekiler
- **13 ders** (L1–L13) konu anlatımı + gömülü C++ / OMNeT++ / sözde kod
- **91 detaylı soru-cevap** (her ders 7)
- **30 soruluk çoktan seçmeli sınav** — otomatik puanlama
- **14 klasik kod sorusu** — boşluk doldurmaca
- **2 çıkmış final sınavı** (2023-24 & 2024-25) — interaktif, cevap anahtarlı

### Konular
| Ders | Konu |
|------|------|
| L1 | OMNeT++ & TicToc'a giriş (DES, modüller, mesajlaşma) |
| L2 | TicToc iyileştirmeleri (EV log, counter, self-message) |
| L3 | TicToc gerçek ağ (channel, .msg, check_and_cast, finish) |
| L4 | Greedy Method (feasible/optimal, optimizasyon, graf temelleri) |
| L5 | Big O notasyonu (hesaplama, sadeleştirme, O/Ω/Θ) |
| L6 | Algoritma analizi — T(n) ve toplam denklemleri |
| L7 | Pandas, DataFrame, Matplotlib |
| L8 | Dijkstra — en kısa yol |
| L9 | Bellman-Ford |
| L10 | Minimum Cost Spanning Tree (Prim & Kruskal) |
| L11 | Graf gezinmeleri — BFS & DFS |
| L12 | Knapsack (sırt çantası) problemi |
| L13 | Topolojik sıralama — Kahn algoritması |

## 🛠️ Yeniden üretme
```bash
cd src
python3 build.py        # -> index.html üretir
```

## ⚠️ Not
Çıkmış sınav soruları taranmış PDF'lerden transkribe edilmiştir; cevap anahtarı hazırlayan
tarafından oluşturulmuştur. Şüpheli durumda hocanın resmi anahtarını esas alın.
