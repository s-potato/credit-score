# Credit Score Classifier

## Môi trường
- VSCode
- python 3.10

## Packages cần cài đặt
- jupyter
- scikit-learn
- seaborn
- matplotlib
- phik
- numpy
- pandas

## Cách chạy
1. Version 1: Mô hình sử dụng dữ liệu chưa qua xử lý
    - Sử dụng file dataset train.csv, được đổi tên thành raw_dataset.csv
    - Chạy file train.ipynb
2. Version 2: Xử lý dữ liệu
    - Sử dụng file dataset train.csv, được đổi tên thành raw_dataset.csv
    - Chạy file clean_data.ipynb, thu được dữ liệu sau khi clean dataset.csv và file lưu lại giá trị của dữ liệu dạng string
    - Chạy file train.ipynb
3. Version 3: Feature Selection
    - Sử dụng dữ liệu đã xử lý, dataset.csv từ Version 2.
    - Chạy file train_correlation_coeffecient.ipynb
4. Version 4: Tuning
    - Sử dụng dữ liệu đã xử lý, dataset.csv từ Version 2.
    - Chạy file train_hyperparams.ipynb
    - Kết quả thu được là mô hình được lưu lại bằng pickle: model.pkl
5. Predict
    - Sử dụng file test.csv làm đầu vào, và model.pkl thu được từ bước train
    - Chạy file dt_predict.ipynb