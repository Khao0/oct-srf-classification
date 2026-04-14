# OCT Subretinal Fluid Classifier — CSC / PCV / VKH

Differentiating CSC, PCV, and VKH disease is clinically challenging because all three conditions produce overlapping patterns of subretinal fluid (SRF) accumulation visible on OCT.

| Label | Full name |
|-------|-----------|
| **CSC** | Central Serous Chorioretinopathy |
| **PCV** | Polypoidal Choroidal Vasculopathy |
| **VKH** | Vogt-Koyanagi-Harada |
| **NoSRF** | No Subretinal Fluid |

This repository implements two distinct deep learning approaches for the automated classification of SRF:
- **Approach 1:** Multi-modal analysis combining single-line OCT with infrared imaging.
> **"Diagnostic Performance of Machine Learning Technology Using Optical Coherence Tomographic Image in Retinal Diseases Presented with Subretinal Fluid"**
> *Khakhai, Panita and Paisarnsrisomsuk, Sarun and Wiratchotisatian, Pitchaya and Tangprasert, Kwankhao and Laovirojjanakul, Wipada — Retina, 2026*
> DOI: [10.1097/IAE.0000000000004708](https://journals.lww.com/retinajournal/abstract/2026/03000/diagnostic_performance_of_machine_learning.13.aspx)

- **Approach 2:** Temporal sequence analysis using multi-line foveal OCT scans.
> **Enhanced Retinal-Choroidal Disorders Classification Model via Temporal Sequence Analysis of OCT Images Across Multiple Lines of Fovea"**
> *Tangprasert, Kwankhao and Wiratchotisatian, Pitchaya and Khakhai, Panita and Laovirojjanakul, Wipada and Paisarnsrisomsuk, Sarun — 2025 ICAIIC, IEEE, 2025*
> DOI: [10.1109/ICAIIC64266.2025.10920750](https://ieeexplore.ieee.org/abstract/document/10920750)

---
## Repository Structure
The repository is organized by methodology. Both approaches utilize a shared inference service for environment management.

#### 1. [Single-Line Analysis](/single-line-analysis/)
*Implementation of the Multi-modal (OCT + Infrared) approach.*
* `data/`: Example data for testing.
* `inference/`: Scripts for model prediction. 
    * *Note: Requires the inference service to be active.*
* `notebook/`: Step-by-step demo of the pipeline.
* `ModelCard.md` : Explaination about the model.

#### 2. [Temporal Sequence Analysis](/temporal-sequence-analysis/)
*Implementation of the Multi-line Fovea Temporal Sequence approach.*
* `data/`
* `inference/`
* `notebook/`
* `ModelCard.md`

#### 3. [Inference Service](/inference_service/)
*Core environment and backend handling.*
This folder manages the environment for the inference process for **both** approaches. Before running any scripts, please configure your environment following the [Inference Service README](/inference_service/SETUP.md).

---

## Intended Use

✅ **Appropriate uses**
- Academic research on retinal disease classification from OCT
- Benchmarking against other automated OCT analysis methods
- Educational demonstration of Grad-CAM explainability in ophthalmology

❌ **Not appropriate for**
- Standalone clinical diagnosis without physician review
- Deployment in patient-facing systems without local validation and regulatory approval
- Use on patient populations significantly different from the Thai clinical cohort

---



## Limitations and Bias

- **Single-centre, single-country data.** The training dataset comes exclusively from one Thai referral hospital. Performance on other ethnic populations or devices from different manufacturers has not been evaluated.
- **No concurrent conditions.** Cases with co-existing retinal pathologies were not included during training.

---

## Ethical Statement

Training data was collected under Institutional Review Board (IRB) approval at Khon Kaen University Hospital, Thailand. All patient data is de-identified and is **not** publicly released due to privacy regulations and hospital ethics policy. Only model weights are distributed through this repository.

Researchers wishing to inquire about dataset access for independent verification should contact the corresponding author listed in the paper.

---

## Citation

If you use this model or code in your research, please cite the original paper:

1. **Diagnostic Performance of Machine Learning Technology Using Optical Coherence Tomographic Image in Retinal Diseases Presented with Subretinal Fluid**
```bibtex

@article{khakhai2026diagnostic,
  title   = {Diagnostic Performance of Machine Learning Technology Using Optical Coherence Tomographic Image in Retinal Diseases Presented with Subretinal Fluid},
  author  = {Khakhai, Panita and Paisarnsrisomsuk, Sarun and Wiratchotisatian, Pitchaya and Tangprasert, Kwankhao and Laovirojjanakul, Wipada},
  journal = {Retina},
  volume  = {46},
  number  = {3},
  pages   = {514--520},
  year    = {2026},
  month   = {March},
  doi     = {10.1097/IAE.0000000000004708}
}

```
2. **Enhanced Retinal-Choroidal Disorders Classification Model via Temporal Sequence Analysis of OCT Images Across Multiple Lines of Fovea**
```bibtex
@INPROCEEDINGS{10920750,
  author={Tangprasert, Kwankhao and Wiratchotisatian, Pitchaya and Khakhai, Panita and Laovirojjanakul, Wipada and Paisarnsrisomsuk, Sarun},
  booktitle={2025 International Conference on Artificial Intelligence in Information and Communication (ICAIIC)}, 
  title={Enhanced Retinal-Choroidal Disorders Classification Model via Temporal Sequence Analysis of OCT Images Across Multiple Lines of Fovea}, 
  year={2025},
  volume={},
  number={},
  pages={0766-0771},
  keywords={Analytical models;Accuracy;Fluids;Sequences;Decision making;Predictive models;Streaming media;Retina;Real-time systems;Diseases;Deep Learning;LSTM;CNN;Medical Image Analysis;Retinal OCT Image;Subretinal Fluid Classification;Central Serous Chorioretinopathy;Polypoidal Choroidal Vasculopathy;Vogt-Koyanagi-Harada},
  doi={10.1109/ICAIIC64266.2025.10920750}
}

```

---

## Contact

For questions about this model, please open an issue on this repository or contact the corresponding author listed in the publication.
- *Khon Kaen University — Department of Computer Engineering, Thailand*
- *hon Kaen University- Department of Statistic, Thailand*
- *Khon Kaen University — Faculty of Medicine, Department of Ophthalmology, Srinagarind Hospital, Thailand*

