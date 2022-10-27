
## create functions
func new --name HttpEndpoint --template "HTTP trigger" --authlevel "anonymous"
func new --template "Azure Queue Storage Trigger" --name QueueTrigger


## Setup

az storage account create --name storagepdc1 --location uksouth --resource-group Cohort22_PauCur_ProjectExercise --sku Standard_LRS

az functionapp create --resource-group Cohort22_PauCur_ProjectExercise --consumption-plan-location uksouth --runtime python --runtime-version 3.8 --functions-version 4 --name PdcAcmeApp1 --storage-account storagepdc1 --os-type linux

## Publish
func azure functionapp publish PdcAcmeApp1


az storage table create --name AcmeTranslations --account-name storagepdc1

func azure functionapp fetch-app-settings PdcAcmeApp1


az storage queue create --name acmesub-translations-queue --account-name storagepdc1
