from flask import Flask,request,render_template,jsonify

from src.pipeline.prediction_pipeline import PredictPipeline,CustomData

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict",methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template("form.html")
    else:
        data=CustomData(     # getting data from form
            carat=float(request.form.get("carat")),
            depth=float(request.form.get("depth")),
            table=float(request.form.get("table")),
            x=float(request.form.get("x")),
            y=float(request.form.get("y")),
            z=float(request.form.get("z")),
            cut=request.form.get("cut"),
            color=request.form.get("color"),
            clarity=request.form.get("clarity")
        )
        final_data=data.get_data_as_dataframe()

        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_data)

        result=round(pred[0],2)    #This takes the first value from pred (a list or array) and rounds it to 2 decimal places.

        return render_template("result.html",final_result=result)  #This shows a web page called result.html.It also sends the rounded result to that page using the variable final_result.

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)