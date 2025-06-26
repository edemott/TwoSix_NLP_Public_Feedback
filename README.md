# Analyzing Public Feedback on Environmental Policies Using NLP

This project is part of **CMSE 495**, the final-year undergraduate capstone course for data science and computational data science majors at Michigan State University (MSU). The course involves team-based projects in collaboration with industry partners, where students develop and deliver data-driven solutions over the semester.

Our team is collaborating with **[Two Six Technologies](https://twosixtech.com/)** on the project **"Analyzing Public Feedback on Environmental Policies Using Natural Language Processing."** The goal is to analyze public responses to environmental policies using NLP techniques. To achieve this, we are utilizing **[Mirrulations](https://github.com/MoravianUniversity/mirrulations)** to collect data from the **[Federal Register](https://www.regulations.gov/)**, and subsequently storing climate related comments in **MongoDB** from federal documents. We then extract comments from the agency 'EPA', and generate embeddings from this data using BERT, perform sentiment analyses using HuggingFace transformers, and then visualize our output with PHATE, and compare it with other well-know dimension reducing models.

### Technologies Used:
- MSU's **High Performance Computing Center (HPCC)** for high-performance computing and database storage.
- **MongoDB** for storing raw documents and **ChromaDB** for managing vector embeddings.
- **BERTopic** for generating sentence embeddings.
- **Transformer** for generating and gauging comment sentiment.
- **PHATE** for visualization and dimensionality reduction of text embeddings . 


## Final Report

The team's [Final Report](https://github.com/wangzey5/TwoSix_Spring25/blob/main/Final%20Report.pdf).

## Final Video

To view the team's final project video, see our [Final Video](https://mediaspace.msu.edu/media/TwoSix+Final+Project+Video/1_g7i7fw71)

## Minimum Viable Product 

To view the team's Minimum Viable Proudct (MVP), see our [MVP Video](https://mediaspace.msu.edu/media/TwoSix-MVP-Video/1_ziff1fki).


## Installation

For installation instructions and the pipeline to run the code please refer to [INSTALL.md](INSTALL.md).


## Authors

- [Emma Fountain](https://github.com/RandumbPurson)
- [Ethan DeMott](https://github.com/edemott)
- [Archan Tulpule](https://github.com/tulpulea)
- [Archisha Bhatt](https://github.com/archishabhatt)
- [Zeyu (Frank) Wang](https://github.com/wangzey5)

## Acknowledgments
This project was developed in collaboration with the TwoSix Technologies. Special thanks to all community partners and course instructors for their support and guidance.
