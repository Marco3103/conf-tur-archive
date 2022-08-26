# Contenuto della repository

Tre cartelle:  
- **dataset**  
	contiene i dataset prodotti dal codice scritto durante il tirocinio, nello specifico contengono tutti degli indici turistici.  
- **notebook e script**  
	contiene sia i notebook che creano i dataset con i dati turistici, sia i notebook con l'analisi dei dati.  
- **prima parte**  
	contiene vario materiale usato nelle prime ore di tirocinio; inutilizzato poi successivamente perchè non più utile


### Contenuto della cartella 'notebook e script'

- **tourist_arrivals.ipynb**: crea un dataset con il numero di arrivi di turisti di uno Stato.
- **WEF_results.ipynb**: effettua lo scraping del report del World Economic Forum per scaricare gli indici turistici
relativi ad uno Stato.
- **google_results.ipynb**: effettua lo scraping di una pagina di ricerca Google, per scaricare il numero di risultati
relativo a quella ricerca.
- **booking_results.ipynb**: effettua lo scraping di una pagina di ricerca Booking, per scaricare il numero di strutture
della città che abbiamo cercato.
- **TripAdvisor_results.ipynb**: effettua lo scraping di una pagina di TripAdvisor, dove è presente il numero di attrazioni
(piazze,musei,teatri ecc...) della città cercata.
- **join_datasets_indexes.ipynb**: crea dei datset dove sono raggruppati gli indici turistici, suddivisi per Stato e per
città.
- **COCI_analysis.ipynb**: analisi dei dati, partendo dalle citazioni di OpenCitations.
- **MAG_analysis.ipynb**: analisi dei dati, partendo dalle citazioni di MAG.

### File utilizzati nei notebook
Nei notebook ho utilizzato dei file in input; evito di caricarli su Github perchè sono troppo pesanti. Al momento si 
trovano tutti su OneDrive.  
Di seguito l'elenco dei file con i link a Onedrive:

- [out_citations_and_conferences_location_ready.csv](https://unimore365-my.sharepoint.com/:u:/g/personal/rmartoglia_unimore_it/EXEe_9fZ9tpIvzvZvl0s9WABZ3IV0xPVnqvUKCXdB9SezQ?e=4vOhy6)
- [unwto-inbound-arrivals-data.xlsx](https://unimore365-my.sharepoint.com/:x:/g/personal/rmartoglia_unimore_it/Eb_f7dvi3lhNhbhLv8NcphkB9OzBQ2L1nHXHpYlMSDhZdA?e=Djalge)
- [WEF_TTCR_2019.pdf](https://unimore365-my.sharepoint.com/:b:/g/personal/rmartoglia_unimore_it/Efe7vTjJMrtJkZ5og4ndqFMB15yVRaZ_jNLhfqVk0OUddA?e=ZPQ6jQ)
- [out_COCI_citations_and_locations_analysis_ready.csv](https://unimore365-my.sharepoint.com/:u:/g/personal/rmartoglia_unimore_it/EaUsn1DPYCNMhOkoQBLj_rUBn-pgmceKfqQ2bnZHa1ThyA?e=B7iscA)
- [out_conference_series_with_core_rank.csv](https://unimore365-my.sharepoint.com/:u:/g/personal/rmartoglia_unimore_it/EcfyyoS9PVRBhZTGMM_0AW8BZMXiak3GkYFxpOU2X-CfIw?e=4zKomG)
- [out_conference_series_with_grin_rank.csv](https://unimore365-my.sharepoint.com/:u:/g/personal/rmartoglia_unimore_it/EXUTdOZ8H8hCqtj1p6_LgBMBrA0nPx-185lmcBabPx75YQ?e=66zTcy)
- [out_MAG_citations_and_locations_analysis_ready.csv](https://unimore365-my.sharepoint.com/:u:/g/personal/rmartoglia_unimore_it/EVWBY8dRQThChb5ADj8wppoBdeYxGguhoNsIYmsYjmc2TA?e=iOAY71)    

Anche i seguenti file sono stati importati nei notebook, ma sono file di indici turistici che ho prodotto nelle varie 
fasi, sono di piccole dimensioni quindi  sono stati caricati nella repo, nella cartella **dataset**:
- all_indexes_by_city.csv
- all_indexes_by_country.csv
- google_results.csv
- booking_results.csv
- tourist_arrivals_by_country_and_year.csv
- wef_results.csv
- TripAdvisor_results.csv 

### Librerie e software utilizzati

Python 3.8.10  
requests 2.22.0  
Pandas 1.3.3  
bs4 4.8.2  
Selenium 4.3.0  
Tutto il lavoro è stato eseguito sul sistema operativo Linux Mint.
