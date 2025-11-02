# R script: HPV Vaccine HTA – literature processing
# Run in VS Code / R terminal

# install.packages(c("revtools","tidyverse","metafor","readr","here"), dependencies = TRUE)

library(tidyverse)
library(readr)

# 1. Read exported PubMed/Embase CSV
refs <- read_csv("data/hpv_search_results.csv")  # TODO: place your exported file

# 2. Deduplicate
refs_clean <- refs %>%
  distinct(title, .keep_all = TRUE)

# 3. Export screening sheet
write_csv(refs_clean, "output/hpv_screening_sheet.csv")

# 4. Meta-analysis placeholder (e.g., VE against HPV 16/18)
# library(metafor)
# dat <- escalc(measure="RR", ai=cases_vacc, bi=total_vacc, ci=cases_control, di=total_control, data=yourdata)
# res <- rma(yi, vi, data=dat, method="REML")
# print(res)
