# Data Files

The following large data files are required to run this project but are not stored in this repository due to size constraints and privacy.
Please note, you need to have an MSU school email to access these.

You can download the files here:


1. [comments.json](https://michiganstate.sharepoint.com/:u:/s/Section_SS25-CMSE-495-001-225215054-EL-32-A26-TwoSix/EXAYysZSTAFEld6TQo7WAGoBMKcPgRCMQbFAVKTIqbuyfQ?e=pPw0UJ) is a an uncleaned json which was retrieved from our MongoDB server using the command "mongoexport"

2. [filtered_comments.csv](https://michiganstate.sharepoint.com/:x:/s/Section_SS25-CMSE-495-001-225215054-EL-32-A26-TwoSix/EQERmIQ3SMNHgFfIE3J77FsBHJUC4tOYg69bBxVq75drWw?e=k2TeXe) is a result of running extract_csv.py on comments.json

3. [df_processed.pkl](https://michiganstate.sharepoint.com/:u:/s/Section_SS25-CMSE-495-001-225215054-EL-32-A26-TwoSix/ES_nJhXQRZ1NpC3NovpkjcsBzzHvO__8SMWWDD3yr5sv0Q?e=6eohg3) is a pickle file (python objects processed into a byte stream) and consists of cleaned comment text and its metadata.
   
4. [data.pkl]() is a pickle file of our comments along with bert-processed embeddings, topics and probabilities.


After downloading, place them in the `data/` directory so that the scripts can find them automatically.
