L = {
"code": "it", "htmllang": "it", "name": "Italiano",
"date": "25 settembre 2026",
"ui": {
    "home": "Home", "privacy": "Privacy", "terms": "Termini", "delete": "Elimina dati",
    "menu": "Pagine", "language": "Lingua", "effective": "Data di entrata in vigore", "contact": "Contatti",
    "summary": "In breve", "toc": "Indice", "legal": "Note legali",
    "by": "Un gioco mobile di Synverse",
    "tagline": "Informativa sulla privacy, termini d’uso ed eliminazione dei dati di Watt Street.",
    "landing": "Watt Street è un gioco idle tycoon in cui porti la luce elettrica in una città in stile 1882. Qui trovi i documenti legali del gioco.",
},
"privacy": {
"title": "Informativa sulla privacy",
"blurb": "Quali dati usa il gioco, perché, e i tuoi diritti.",
"intro": """<p>Questa Informativa sulla privacy spiega come <b>Synverse</b> (“noi”) tratta le informazioni quando giochi a <b>%GAME%</b> (“il gioco”, pacchetto <code>%PKG%</code>) su Android o iOS. Il gioco è pensato per funzionare con il minor numero possibile di dati: non c’è registrazione e non ti chiediamo mai nome, indirizzo email o numero di telefono.</p>""",
"summary": [
    "Non servono account né login. Il gioco crea un ID giocatore (Player ID) anonimo e casuale tramite Unity Gaming Services.",
    "I progressi della tua città sono salvati sul dispositivo e copiati su Unity Cloud Save con quell’ID giocatore.",
    "Non raccogliamo nome, email, telefono, contatti, foto, posizione precisa, fotocamera o microfono.",
    "Gli annunci, se presenti, sono video con premio facoltativi di Google AdMob. Google può usare identificatori del dispositivo per la pubblicità, con il tuo consenso ove richiesto dalla legge.",
    "Puoi chiederci in qualsiasi momento di eliminare i tuoi dati nel cloud: vedi <a href=\"%DELETE_LINK%\">Elimina i tuoi dati</a>.",
],
"sections": [
("Titolare del trattamento", """<p>Il titolare del trattamento è Synverse, editore di %GAME%. Puoi contattarci all’indirizzo %EMAIL%.</p>"""),
("Informazioni trattate dal gioco", """<h3>a) Dati salvati solo sul tuo dispositivo</h3>
<p>Il gioco conserva il tuo salvataggio (progressi della città, edifici, valuta di gioco, orari usati per i guadagni offline) e le tue impostazioni (musica, effetti sonori, vibrazione, lingua, avanzamento del tutorial e contatori di attesa degli annunci) nello spazio privato dell’app sul dispositivo. Non abbiamo accesso a questi dati. La vibrazione (feedback aptico) è gestita localmente dal dispositivo e non invia nulla.</p>
<h3>b) ID giocatore anonimo (Unity Authentication)</h3>
<p>Quando giochi online, il gioco accede in modo anonimo con Unity Authentication. Unity assegna un <b>ID giocatore</b> casuale e token di sessione. L’ID non è collegato al tuo nome, email o telefono. I servizi Unity usano anche un identificatore di installazione casuale e dati tecnici come indirizzo IP, tipo di dispositivo, sistema operativo e versione dell’app per fornire il servizio.</p>
<h3>c) Backup nel cloud (Unity Cloud Save)</h3>
<p>Una copia del salvataggio (gli stessi dati di progresso descritti sopra, più identificatori tecnici di revisione) è conservata su Unity Cloud Save con il tuo ID giocatore, per poter ripristinare la tua città. Il gioco sincronizza periodicamente il backup mentre giochi.</p>
<h3>d) Contenuti di gioco (Unity Remote Config)</h3>
<p>Il gioco scarica il catalogo delle missioni da Unity Remote Config. Questa richiesta usa il tuo ID giocatore e i dati tecnici necessari a fornire i contenuti; non invia il tuo salvataggio.</p>
<h3>e) Collegamento facoltativo dell’account (se disponibile)</h3>
<p>Se il gioco offre di collegare i progressi a un account Unity, l’accesso avviene sulla pagina di Unity. Non vediamo né conserviamo mai la tua password; Unity comunica al gioco solo un identificatore dell’account per ripristinare il salvataggio su un altro dispositivo.</p>
<h3>f) Annunci (Google AdMob, se/quando disponibili)</h3>
<p>Il gioco può offrire <b>annunci con premio facoltativi</b>: un annuncio parte solo quando tocchi per guardarlo in cambio di un premio nel gioco. Non ci sono annunci obbligatori. Gli annunci sono forniti da Google AdMob, che può raccogliere e trattare l’identificatore pubblicitario del dispositivo (ID pubblicità Android / IDFA di Apple), indirizzo IP, informazioni su dispositivo e app e dati di interazione con gli annunci per mostrare, misurare e personalizzare gli annunci e prevenire le frodi. Da Android 13 il gioco dichiara l’autorizzazione <code>AD_ID</code> affinché AdMob possa leggere l’ID pubblicità; puoi reimpostarlo o eliminarlo nelle impostazioni del dispositivo.</p>
<p>Nello Spazio economico europeo, nel Regno Unito e in Svizzera, il gioco chiede il tuo consenso tramite la piattaforma di messaggistica per gli utenti (UMP) di Google prima di mostrare annunci personalizzati; se rifiuti, Google può comunque mostrare annunci non personalizzati. Su iOS l’identificatore pubblicitario viene usato solo se lo consenti nella richiesta di Trasparenza sul tracciamento delle app (ATT) di Apple. Per saperne di più: <a href="%G_PARTNER%">In che modo Google utilizza le informazioni di siti o app che utilizzano i suoi servizi</a> e le <a href="%G_PRIV%">Norme sulla privacy di Google</a>.</p>
<h3>g) Acquisti in-app (se/quando disponibili)</h3>
<p>Se il gioco offre acquisti, i pagamenti sono gestiti interamente da Google Play o dall’App Store di Apple. Non riceviamo mai i dati della tua carta o del tuo conto. Riceviamo solo una conferma d’acquisto (ad esempio ID prodotto e ID ordine/transazione) per consegnarti ciò che hai acquistato.</p>
<h3>h) Quando ci scrivi</h3>
<p>Se ci invii un’email, riceviamo il tuo indirizzo e il contenuto del messaggio e li usiamo solo per risponderti.</p>
<h3>i) Cosa non raccogliamo</h3>
<p>Non raccogliamo nome, indirizzo email (salvo che tu ci scriva), numero di telefono, contatti, foto o file, posizione precisa o approssimativa tramite i servizi di localizzazione, né dati di fotocamera o microfono. Il gioco non ha chat né funzioni social. Non usiamo il servizio Unity Analytics. Se il gioco si arresta in modo anomalo o incontra un errore, un rapporto di crash (modello del dispositivo, sistema operativo, versione dell’app e traccia tecnica dell’errore, senza dati personali) viene inviato a Unity (Cloud Diagnostics) per permetterci di correggere i bug. Il motore Unity stesso può inviare a Unity informazioni tecniche limitate (ad esempio modello del dispositivo, sistema operativo e versione del motore), come descritto nell’<a href="%U_PRIV%">informativa sulla privacy di Unity</a>.</p>"""),
("Finalità e basi giuridiche", """<ul>
<li><b>Far funzionare il gioco e conservare i progressi</b> (salvataggio locale, backup cloud, accesso anonimo, download delle missioni): necessario per fornire il servizio richiesto (art. 6.1.b GDPR).</li>
<li><b>Sicurezza, prevenzione degli abusi e stabilità del servizio</b> (ad esempio limiti alle richieste e log tecnici conservati da Unity): nostro legittimo interesse (art. 6.1.f GDPR).</li>
<li><b>Annunci personalizzati</b>: il tuo consenso ove richiesto (art. 6.1.a GDPR), revocabile in qualsiasi momento. Annunci non personalizzati e prevenzione delle frodi pubblicitarie: legittimo interesse.</li>
<li><b>Rispondere alle tue richieste e adempiere agli obblighi di legge</b>: obbligo legale e legittimo interesse (art. 6.1.c e f GDPR).</li>
</ul>
<p>Non usiamo i tuoi dati per decisioni automatizzate che producano effetti giuridici o analogamente significativi.</p>"""),
("Con chi li condividiamo", """<ul>
<li><b>Unity Technologies</b> (Authentication, Cloud Save, Remote Config) ospita l’ID giocatore, il backup cloud e i contenuti di gioco per nostro conto, come responsabile del trattamento. Vedi l’<a href="%U_PRIV%">informativa sulla privacy di Unity</a>.</li>
<li><b>Google</b> (AdMob), se sono presenti annunci, come descritto sopra. Per gli annunci personalizzati Google agisce come titolare autonomo dei dati che raccoglie. Vedi le <a href="%G_PRIV%">Norme sulla privacy di Google</a>.</li>
<li><b>Google Play / Apple</b>, per download, aggiornamenti ed eventuali acquisti, secondo le rispettive informative.</li>
<li><b>Autorità</b>, solo se richiesto dalla legge.</li>
</ul>
<p>Non vendiamo le tue informazioni personali in cambio di denaro. Secondo alcune leggi statali degli USA (ad esempio la California), consentire ad AdMob di mostrare annunci personalizzati può costituire una “condivisione” per pubblicità comportamentale cross-context; puoi opporti come indicato nella sezione 7.</p>"""),
("Trasferimenti internazionali", """<p>Unity e Google possono trattare dati su server al di fuori del tuo paese, anche negli Stati Uniti. Tali trasferimenti si basano su garanzie adeguate, come le clausole contrattuali tipo della Commissione europea.</p>"""),
("Per quanto tempo li conserviamo", """<ul>
<li><b>Dati sul dispositivo</b>: finché non elimini il gioco o ne cancelli i dati.</li>
<li><b>Backup cloud e ID giocatore</b>: finché usi il gioco. Li eliminiamo su richiesta (vedi <a href="%DELETE_LINK%">Elimina i tuoi dati</a>) entro 30 giorni dalla verifica della richiesta.</li>
<li><b>Email di assistenza</b>: fino a 12 mesi dopo la chiusura della richiesta, salvo termini di legge più lunghi.</li>
<li><b>Dati pubblicitari</b>: conservati da Google secondo le proprie norme.</li>
</ul>"""),
("Scelte e diritti", """<p>Ai sensi del GDPR hai diritto di accesso, rettifica, cancellazione, limitazione, opposizione e portabilità, nonché di revocare il consenso in qualsiasi momento. I residenti in California e in altri stati degli USA possono chiedere di conoscere, eliminare e correggere le proprie informazioni e opporsi alla loro “vendita” o “condivisione”. Gli utenti in Turchia hanno i diritti previsti dall’art. 11 della legge KVKK. Non ti discrimineremo per l’esercizio di questi diritti.</p>
<p><b>Come esercitarli:</b> scrivi a %EMAIL% indicando l’ID giocatore mostrato nel gioco in <i>Impostazioni › Account e cloud</i>. Poiché non conosciamo il tuo nome né la tua email, è l’ID giocatore a permetterci di trovare i tuoi dati. Rispondiamo entro un mese.</p>
<p><b>Annunci:</b> modifica il consenso pubblicitario dalle opzioni sulla privacy del gioco (mostrate in SEE, Regno Unito e Svizzera), reimposta o elimina l’ID pubblicità nelle impostazioni del dispositivo oppure gestisci gli annunci in <a href="%G_ADS%">Il mio Centro annunci</a>. Su iOS puoi disattivare il tracciamento in Impostazioni › Privacy e sicurezza › Tracciamento.</p>
<p>Puoi anche proporre reclamo a un’autorità di controllo (in Italia, il Garante per la protezione dei dati personali; <a href="%EDPB%">elenco delle autorità</a>).</p>"""),
("Eliminare i tuoi dati", """<p>Disinstallare il gioco rimuove tutti i dati salvati sul dispositivo. Per eliminare il backup cloud e l’ID giocatore anonimo, segui i passaggi della pagina <a href="%DELETE_LINK%">Elimina i tuoi dati</a>.</p>"""),
("Minori", """<p>%GAME% è destinato a giocatori di almeno 13 anni e non è rivolto a bambini sotto i 13 anni. In conformità con la legge statunitense COPPA, non raccogliamo consapevolmente informazioni personali da bambini sotto i 13 anni. Se sei un genitore o tutore e ritieni che tuo figlio sotto i 13 anni abbia usato il gioco, scrivici a %EMAIL% ed elimineremo i dati relativi. Dove la legge locale fissa un’età più alta per il consenso al trattamento dei dati (14 anni in Italia, fino a 16 in alcuni paesi dell’UE), i giocatori più giovani dovrebbero accettare annunci personalizzati solo con il permesso di un genitore.</p>"""),
("Sicurezza", """<p>I dati scambiati tra il gioco e i servizi di Unity o Google sono cifrati in transito (HTTPS/TLS). I dati sul dispositivo restano nello spazio privato dell’app, protetto dal sistema operativo. Nessun sistema è perfettamente sicuro, ma limitiamo ciò che raccogliamo in modo che ci sia poco da proteggere.</p>"""),
("Modifiche a questa informativa", """<p>Possiamo aggiornare questa informativa quando il gioco cambia (ad esempio con l’aggiunta di annunci o acquisti). Aggiorneremo la data qui sopra e, per le modifiche importanti, ti avviseremo nel gioco.</p>"""),
("Contatti", """<p>Synverse — %EMAIL%<br>Indica “%GAME%” nell’oggetto.</p>"""),
],
},
"terms": {
"title": "Termini d’uso",
"blurb": "Le regole essenziali per giocare.",
"intro": """<p>I presenti Termini d’uso (“Termini”) sono un accordo tra te e <b>Synverse</b> per il gioco mobile <b>%GAME%</b>. Scaricando o giocando accetti questi Termini e la nostra <a href="%PRIVACY_LINK%">Informativa sulla privacy</a>. Se non sei d’accordo, non usare il gioco.</p>""",
"sections": [
("Chi può giocare", """<p>Devi avere almeno 13 anni. Se sei minorenne nel tuo paese di residenza, ti serve il permesso di un genitore o tutore.</p>"""),
("La tua licenza", """<p>Ti concediamo una licenza personale, non esclusiva, non trasferibile e revocabile per scaricare il gioco e giocarci sui tuoi dispositivi per scopi non commerciali. Il gioco, il suo codice, la grafica, la musica, i testi e i marchi appartengono a Synverse o ai suoi licenzianti. Non puoi copiare, vendere, noleggiare, modificare, decompilare o ridistribuire il gioco, salvo quanto espressamente consentito dalla legge.</p>"""),
("Oggetti e valuta di gioco", """<p>Denaro, oggetti, potenziamenti e progressi di gioco non hanno valore reale, non possono essere convertiti in denaro reale e ti sono concessi in licenza, non venduti. Possiamo bilanciarli, modificarli o rimuoverli con gli aggiornamenti.</p>"""),
("Acquisti (se/quando disponibili)", """<p>Se il gioco offre acquisti, questi avvengono tramite Google Play o l’App Store di Apple e sono soggetti ai rispettivi termini e politiche di rimborso. I tuoi diritti di consumatore previsti dalla legge restano invariati.</p>"""),
("Annunci", """<p>Il gioco può offrire annunci con premio facoltativi. I contenuti pubblicitari sono forniti da terzi (Google AdMob) e non siamo responsabili di prodotti o siti di terzi mostrati negli annunci.</p>"""),
("Uso corretto", """<p>Non usare il gioco per scopi illeciti, non attaccare né sovraccaricare i nostri servizi o quelli dei nostri fornitori e non ostacolare l’uso del servizio da parte di altri giocatori.</p>"""),
("Backup cloud e disponibilità", """<p>Il backup cloud è offerto per comodità. Lavoriamo per renderlo affidabile, ma non possiamo garantire che il gioco o i suoi servizi online siano sempre disponibili e privi di errori, né che i dati non vadano mai persi. Possiamo aggiornare, modificare o interrompere il gioco o qualsiasi funzione.</p>"""),
("Esclusione di responsabilità", """<p>Il gioco è fornito “così com’è” e “come disponibile”. Nei limiti consentiti dalla legge, Synverse non risponde di danni indiretti, perdita di dati o perdita di oggetti di gioco. Nulla in questi Termini limita responsabilità non limitabili per legge né i tuoi diritti inderogabili di consumatore.</p>"""),
("Cessazione", """<p>Puoi smettere di usare il gioco in qualsiasi momento disinstallandolo. Possiamo sospendere o interrompere il tuo accesso in caso di grave violazione di questi Termini.</p>"""),
("Dispositivi Apple", """<p>Se hai scaricato il gioco dall’App Store di Apple, si applica anche il <a href="%APPLE_EULA%">Contratto di licenza standard per l’utente finale</a> di Apple. Apple non è responsabile del gioco né della relativa assistenza, e Apple e le sue controllate sono terzi beneficiari di questi Termini.</p>"""),
("Legge applicabile e modifiche", """<p>Questi Termini sono regolati dalla legge della Repubblica di Turchia. Se sei un consumatore, mantieni la tutela delle norme inderogabili del tuo paese di residenza e puoi agire lì. Possiamo aggiornare questi Termini; la data qui sopra indica la versione in vigore e continuare a giocare significa accettare l’aggiornamento.</p>"""),
("Contatti", """<p>Synverse — %EMAIL%</p>"""),
],
},
"delete": {
"title": "Elimina i tuoi dati",
"blurb": "Come eliminare i dati cloud di Watt Street e il tuo ID giocatore.",
"intro": """<p>Questa pagina spiega come eliminare i dati di <b>%STORE%</b> di <b>Synverse</b> (pacchetto <code>%PKG%</code>). Il gioco non richiede registrazione: usa un ID giocatore anonimo di Unity Gaming Services e un backup cloud della tua città.</p>""",
"sections": [
("Richiedere l’eliminazione", """<ol>
<li>Apri il gioco e tocca <b>Impostazioni</b> (icona ingranaggio) › <b>Account e cloud</b>. Copia il tuo <b>ID giocatore</b>.</li>
<li>Scrivi a %EMAIL% con oggetto <b>“%GAME% – eliminazione dati”</b> indicando il tuo ID giocatore.</li>
<li>Eliminiamo i tuoi dati entro 30 giorni e te lo confermiamo via email.</li>
</ol>
<p>Senza ID giocatore potremmo non riuscire a trovare i tuoi dati, perché non conosciamo il tuo nome né il tuo indirizzo email.</p>"""),
("Cosa viene eliminato", """<ul>
<li>Il salvataggio cloud (progressi della città) conservato su Unity Cloud Save.</li>
<li>L’ID giocatore anonimo e il relativo record di accesso in Unity Authentication.</li>
</ul>
<p>L’eliminazione è definitiva: i progressi nel cloud non potranno essere ripristinati.</p>"""),
("Cosa può essere conservato", """<p>Conserviamo la tua email e la richiesta fino a 12 mesi come prova della gestione, salvo termini di legge più lunghi. I log tecnici di Unity vengono eliminati secondo i tempi di Unity. I dati raccolti da Google per la pubblicità sono sotto il controllo di Google.</p>"""),
("Dati sul dispositivo", """<p>Disinstalla il gioco o cancellane i dati nelle impostazioni del dispositivo per rimuovere salvataggio e impostazioni dal telefono. Questo non elimina il backup cloud; richiedilo come indicato sopra.</p>"""),
("Dati pubblicitari", """<p>Per reimpostare o eliminare l’ID pubblicità usa le impostazioni del dispositivo (Android: Impostazioni › Privacy › Annunci; iOS: Impostazioni › Privacy e sicurezza › Tracciamento). Puoi gestire i dati pubblicitari di Google in <a href="%G_ADS%">Il mio Centro annunci</a>.</p>"""),
],
},
}
