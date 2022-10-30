# Azure Function setup

## Create Azure Functions app in local folder

`func new --name HttpEndpoint --template "HTTP trigger" --authlevel "anonymous"`

`func new --name QueueTrigger --template "Azure Queue Storage Trigger"`

## Setup

`az storage account create --name storagepdc1 --location uksouth --resource-group Cohort22_PauCur_ProjectExercise --sku Standard_LRS`

`az storage table create --name AcmeTranslations --account-name storagepdc1`

`az storage table create --name AcmeTranslated --account-name storagepdc1`

`az storage queue create --name acmesub-translations-queue --account-name storagepdc1`

`az functionapp create --resource-group Cohort22_PauCur_ProjectExercise --consumption-plan-location uksouth --runtime python --runtime-version 3.8 --functions-version 4 --name PdcAcmeApp1 --storage-account storagepdc1 --os-type linux`

## Get Settings from Azure

`func azure functionapp fetch-app-settings PdcAcmeApp1`

## Run Locally

`func start`

## Publish

`func azure functionapp publish PdcAcmeApp1`
