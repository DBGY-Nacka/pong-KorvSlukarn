[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16466407&assignment_repo_type=AssignmentRepo)
# Pong

## Uppgiften

Du ska återskapa det klassiska spelet Pong.

Pong är ett tennisliknande spel där två spelare spelar mot varandra. Med varsin "paddle" ska spelarna träffa bollen och få den att åka över på motspelarens planhalva.

Passerar bollen motstående spelares långsida så tilldelas den andra poäng.

Alltså, spelar A får bollen att gå över spelare B's långsida, då inkasserar spelare A en poäng.

Spelet pågår antingen tills en timer räknat ner till noll, eller tills någon nått en viss poäng. Du bestämmer.

Spelarnas paddlar kan endast röra sig lodrätt, alltså upp och ner. Den kan inte lämna sin kant för att träffa bollen tidigare. Gör så att ena spelarens paddel rör sig med W och A medan den andra med pil upp och pil ner.

## Krav

I denna uppgift så bedöms klasser, gränssnitt samt kodstil.

__Tänk på att din kod ska pushas varje gång du arbetat med den, dvs efter varje lektion, minst.__

### Uppgiftskrav

Fyll i klasserna __ball__, __paddle__ och __scoreboard__ med relevant kod. Denna skall vara objektorienterad, dvs. arv och klasser ska utnyttjas.

Spelet ska börja efter att man svarat på en prompt (kanske vad spelarna heter?), därefter skapas bollen på mitten av planen med en slumpmässig riktning.

Passerar en boll en långsida får den motstående spelaren en poäng.

Poängen bör redovisas högst upp på skärmen.

Har du en timer ska den visas också.

### Betygskrav

#### Betyget E

Spelet ska gå att spela, dvs det ska finnas två paddlar och en boll som går mellan de två långsidorna (höger och vänster).

Passerar bollen någon av sidorna ska bollen förflytta sig till mitten och spelet börjar om.

#### Betyget C

Samma som för E, men det ska även finnas en Scoreboard, där spelarnas namn (hårdkodade eller dynamiska) visas hela tiden samt deras poäng.

När spelet är över skrivs den vinnande spelaren ut på skärmen, liksom slutresultatet.

Timer får gärna vara inkluderat.

Din kod ska ha läsbara variabel-, funktions- och klassnamn för att underlätta för andra att läsa din kod. Likaså ska kommentarer finnas där det behövs.

