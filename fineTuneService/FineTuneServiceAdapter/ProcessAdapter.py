



test_process = FtProcess()

for question in QUESTION_LIST:

    request_completion = test_process.createRequestFromTemplate(question)

    train_completion = test_process.getTrainCompletion(request_completion)

    train_dataset = test_process.createTrainDataset(train_completion)

    dataset_path = test_process.saveDatasetFile(train_dataset)

saveSourceObject('process', test_process.__dict__)