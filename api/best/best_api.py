# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("../api/best/best_api")

# Create input/output pydantic models
input_model = create_model("../api/best/best_api_input", **{'loc_og_t2o_mou': 0.0, 'std_og_t2o_mou': 0.0, 'loc_ic_t2o_mou': 0.0, 'arpu_6': 116.6050033569336, 'arpu_7': 283.9200134277344, 'arpu_8': 636.9400024414062, 'onnet_mou_6': 104.70999908447266, 'onnet_mou_7': 97.04000091552734, 'onnet_mou_8': 311.30999755859375, 'offnet_mou_6': 46.88999938964844, 'offnet_mou_7': 296.3399963378906, 'offnet_mou_8': 818.2100219726562, 'roam_ic_mou_6': 36.880001068115234, 'roam_ic_mou_7': 1.8300000429153442, 'roam_ic_mou_8': 0.0, 'roam_og_mou_6': 151.8300018310547, 'roam_og_mou_7': 9.210000038146973, 'roam_og_mou_8': 0.0, 'loc_og_t2t_mou_6': 0.0, 'loc_og_t2t_mou_7': 2.700000047683716, 'loc_og_t2t_mou_8': 10.9399995803833, 'loc_og_t2m_mou_6': 0.0, 'loc_og_t2m_mou_7': 43.11000061035156, 'loc_og_t2m_mou_8': 95.66000366210938, 'loc_og_t2f_mou_6': 0.0, 'loc_og_t2f_mou_7': 0.0, 'loc_og_t2f_mou_8': 0.0, 'loc_og_t2c_mou_6': 0.0, 'loc_og_t2c_mou_7': 5.389999866485596, 'loc_og_t2c_mou_8': 0.0, 'loc_og_mou_6': 0.0, 'loc_og_mou_7': 45.810001373291016, 'loc_og_mou_8': 106.61000061035156, 'std_og_t2t_mou_6': 0.0, 'std_og_t2t_mou_7': 87.33000183105469, 'std_og_t2t_mou_8': 300.3599853515625, 'std_og_t2m_mou_6': 0.0, 'std_og_t2m_mou_7': 237.55999755859375, 'std_og_t2m_mou_8': 722.5399780273438, 'std_og_t2f_mou_6': 0.0, 'std_og_t2f_mou_7': 0.0, 'std_og_t2f_mou_8': 0.0, 'std_og_t2c_mou_6': 0.0, 'std_og_t2c_mou_7': 0.0, 'std_og_t2c_mou_8': 0.0, 'std_og_mou_6': 0.0, 'std_og_mou_7': 324.8900146484375, 'std_og_mou_8': 1022.9099731445312, 'isd_og_mou_6': 0.0, 'isd_og_mou_7': 0.0, 'isd_og_mou_8': 0.0, 'spl_og_mou_6': 0.0, 'spl_og_mou_7': 13.84000015258789, 'spl_og_mou_8': 6.690000057220459, 'og_others_6': 0.0, 'og_others_7': 0.0, 'og_others_8': 0.0, 'total_og_mou_6': 0.0, 'total_og_mou_7': 384.55999755859375, 'total_og_mou_8': 1136.22998046875, 'loc_ic_t2t_mou_6': 0.0, 'loc_ic_t2t_mou_7': 1.5800000429153442, 'loc_ic_t2t_mou_8': 45.65999984741211, 'loc_ic_t2m_mou_6': 0.0, 'loc_ic_t2m_mou_7': 46.33000183105469, 'loc_ic_t2m_mou_8': 107.38999938964844, 'loc_ic_t2f_mou_6': 0.0, 'loc_ic_t2f_mou_7': 0.0, 'loc_ic_t2f_mou_8': 0.0, 'loc_ic_mou_6': 0.0, 'loc_ic_mou_7': 47.90999984741211, 'loc_ic_mou_8': 153.05999755859375, 'std_ic_t2t_mou_6': 0.0, 'std_ic_t2t_mou_7': 0.0, 'std_ic_t2t_mou_8': 5.360000133514404, 'std_ic_t2m_mou_6': 0.0, 'std_ic_t2m_mou_7': 17.93000030517578, 'std_ic_t2m_mou_8': 82.02999877929688, 'std_ic_t2f_mou_6': 0.0, 'std_ic_t2f_mou_7': 0.0, 'std_ic_t2f_mou_8': 0.0, 'std_ic_t2o_mou_6': 0.0, 'std_ic_t2o_mou_7': 0.0, 'std_ic_t2o_mou_8': 0.0, 'std_ic_mou_6': 0.0, 'std_ic_mou_7': 17.93000030517578, 'std_ic_mou_8': 87.38999938964844, 'total_ic_mou_6': 0.0, 'total_ic_mou_7': 67.43000030517578, 'total_ic_mou_8': 259.7900085449219, 'spl_ic_mou_6': 0.0, 'spl_ic_mou_7': 0.0, 'spl_ic_mou_8': 0.0, 'isd_ic_mou_6': 0.0, 'isd_ic_mou_7': 0.0, 'isd_ic_mou_8': 19.1299991607666, 'ic_others_6': 0.0, 'ic_others_7': 1.5800000429153442, 'ic_others_8': 0.20000000298023224, 'total_rech_num_6': 4.0, 'total_rech_num_7': 8.0, 'total_rech_num_8': 18.0, 'total_rech_amt_6': 170.0, 'total_rech_amt_7': 336.0, 'total_rech_amt_8': 726.0, 'max_rech_amt_6': 120.0, 'max_rech_amt_7': 120.0, 'max_rech_amt_8': 130.0, 'last_day_rch_amt_6': 50.0, 'last_day_rch_amt_7': 30.0, 'last_day_rch_amt_8': 20.0, 'total_rech_data_6': 0.0, 'total_rech_data_7': 0.0, 'total_rech_data_8': 0.0, 'max_rech_data_6': 0.0, 'max_rech_data_7': 0.0, 'max_rech_data_8': 0.0, 'av_rech_amt_data_6': 0.0, 'av_rech_amt_data_7': 0.0, 'av_rech_amt_data_8': 0.0, 'vol_2g_mb_6': 0.0, 'vol_2g_mb_7': 0.0, 'vol_2g_mb_8': 0.0, 'vol_3g_mb_6': 0.0, 'vol_3g_mb_7': 0.0, 'vol_3g_mb_8': 0.0, 'night_pck_user_6': 0.0, 'night_pck_user_7': 0.0, 'night_pck_user_8': 0.0, 'monthly_2g_6': 0.0, 'monthly_2g_7': 0.0, 'monthly_2g_8': 0.0, 'sachet_2g_6': 0.0, 'sachet_2g_7': 0.0, 'sachet_2g_8': 0.0, 'monthly_3g_6': 0.0, 'monthly_3g_7': 0.0, 'monthly_3g_8': 0.0, 'sachet_3g_6': 0.0, 'sachet_3g_7': 0.0, 'sachet_3g_8': 0.0, 'fb_user_6': 0.0, 'fb_user_7': 0.0, 'fb_user_8': 0.0, 'aon': 544.0, 'aug_vbc_3g': 0.0, 'jul_vbc_3g': 0.0, 'jun_vbc_3g': 0.0})
output_model = create_model("../api/best/best_api_output", churn_probability_prediction=0)


# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"churn_probability_prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
