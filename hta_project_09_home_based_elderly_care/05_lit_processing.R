# Home-based elderly care HTA – literature processing
library(tidyverse)
dir.create("output", showWarnings = FALSE)
if (file.exists("data/elderly_homecare_search_results.csv")) {
  refs <- read_csv("data/elderly_homecare_search_results.csv")
  refs_clean <- refs %>% distinct(title, .keep_all = TRUE)
  write_csv(refs_clean, "output/elderly_homecare_screening_sheet.csv")
} else {
  tibble(title=character(), year=integer(), source=character()) %>%
    write_csv("output/elderly_homecare_screening_sheet.csv")
}
