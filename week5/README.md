Interpretations

Disclaimer:
These interpretations are based on Merryn’s plots, which may differ from the other uploaded plots due to different parameters entered in the shiny app

PCA: 
Based on the principal component analysis, it becomes clear that infection drives transcriptomic changes within the given samples. The Series15_COVID19Lung replicates 1 and 2 are both explained by PC2, while Series15_HealthyLungBiopsy 1 and 2 were not infected but are also mainly explained by PC2 indicating a similar overall gene expression profile, with a significant influence of the infection being demonstrated due to the distance between them. 
 
Differential gene expression analysis: 
Based on the volcano plot there are many upregulated genes and a few down-regulated ones in the infected compared to the non-infected condition at an adjusted p-value threshold of 0.05 and an absolute log 2fold change cutoff of 1. Which goes in line with immune related genes activating in response to viral antigens. Of particular interest the gene KCNMBI with a log2FC of 24 and a p value of 8.39 ^-14 may be of interest and would justify further research, for instance into its function and pharmacologic interventions targeting KCNMBI, based on its function, since its log2FC is more than twice as high as the next highest at 10.7. The gene labeled BGN is decreased the most in the infected condition, with a IGLL5 of almost 24, indicating a large reduction in transcription. This gene may also be involved in classical cellular responses to viral infections, since it may normally inhibit antiviral responses. 

Heatmap:
Yellow indicates the mock and the purple the infected condition, which cluster quite well across samples. The y axis indicates the top 50 genes that variate the most and the x axis shows the samples in question. This plot can supply which genes react as a cluster in which conditions giving an overview that can supply detail if needed. Here too huge changes in gene expression compared to the averages can be observed based on the intensity of the colours that indicate Z-scores. Most blocks of colour being consistent across multiple samples indicates reliable differential expression as opposed to random noise in the data.
