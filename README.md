[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7008647&assignment_repo_type=AssignmentRepo)


# ZASVRŠNI PROJEKT - FLASK WEB APLIKACIJA
#### autor : Dino Barešić

* Aplikacija se sastoji od više stranica koje predstavljaju aplikaciju za rezervaciju apartmana.Osnovna namjena aplikacije je primiti rezervaciju spremiti je u bazu podataka te nakon "odglumljenog" plaćanja poslati mail potvrde rezervacije. Podaci se spremaju iz Flask forme na stranici (book-now.html) u sqlite bazu podataka. Nakon "plaćanja" u bazi podataka se mijenja red te iste rezervacije iz "not paid" u "paid" te se šalje mail potvrde. Forma na stranici (contact.html) također šalje mail na mail apartmana koji je napravljen za test. Aplikacija je napravljena za jednog korisnika tj. samo gosta jer je takvog sadržaja.
<br>

### Pokretanje aplikacije
#### 1. Ulazimo u direktorij (zavrsni-projekt-webapp) te pokrenemo "app.py"
#### 2. 