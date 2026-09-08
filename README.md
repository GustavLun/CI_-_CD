## 📋 Uppgifter

| # | Uppgift   | Beskrivning                                                      | Status |
|---|-----------|------------------------------------------------------------------|--------|
| 1 | Uppgift:1 |              | 🔴 Ej påbörjad |
| 2 | Uppgift:2 | | 🔴 Ej påbörjad |
| 3 | Uppgift:3 |       | 🔴 Ej påbörjad |
### Status
- 🟢 **Klart**
- 🟡 **Halvvägs klar**
- 🔴 **Ej påbörjad**

# Diskutera tillsammans
Frågorna utgår från innehållet i presentationen.

1. Vilka fördelar kan du se med CI & CD på din arbetsplats?
Du som inte arbetar: hur skulle du vilja att det fungerade på din framtida arbetsplats?

2. Vad är poängen med linting?

3. Hur arbetar man med git och flera branches inom ett team? Skulle du vilja ända något på din arbetsplats?

4. Vad är en pull request? (kan sparas till nästa vecka)

---

1. De stora fördelarna med CICD på min arbetsplats är hur vi alla kan vara effektiva från olika håll hela tiden. 
   vi kan alla jobba i egna bransches, pusha, merga, pulla från dev och aktivt komma framåt utan större problem. 
   uppstår problem tillåter git oss att enkelt backtracka senaste commits för att hitta vilken commit som skapade alla problem.
   För mig som testare fungerar det också lättare att testa specifika features då jag kan byta till specifika bransches där jag kan testa folk features i isolerade miljöer.
---
2. linting är ett redskap som ser till att utvecklingsteamet upprätthåller en specifik kodstandard. Den kan rapportera onödig / oanvänd kod
för att tillåta programmera att städa upp i koden och göra den med lättläslig. Summerat den aggerar inte bara som ett verktyg för att hitta fel i koden
den går mer in på djupet och flaggar och koden på något vis har avikelser som inte används eller inte uppfyller den satta kodstandarden.
---
3. I min bransch (spelindustrin) och många andra används git för att tillåta folk att jobba på olika saker från olika håll utan att påverka hela produkten.
på mitt jobb sitter alla i sin egna branch, vi jobbar separat på egna saker, när vi är klara pushas sakerna till bår dev branch. 
dev branchen i detta fall aggerar som en test branch som skall vara som en spegling av main branchen. När man når en milestone som är stabil på dev, mergas den till main.
målet är såklart att när projektet är klart är det main branchen som publiceras.
---
4. 
   

