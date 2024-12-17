from utils import get_llm_output

ex_acc_data = {'x':[-0.32,-2.27,-1.77,-1.14,-1.12,-0.63,-0.53,-0.6,-1.05,-3.01,-3.78,-3.2,-3.,-2.14,-2.11,-1.74,-2.75,-4.57,-2.9,-2.65,-2.37,-1.89,-0.76,-4.22,-4.38,-2.76,-2.65,-1.71,-1.59,-1.7,-3.99,-3.73,-2.77,-2.23,-1.66,-1.41,-3.24,-4.81,-3.44,-2.76,-2.09,-2.02,-1.06,-4.01,-4.49,-3.16,-2.21,-2.04,-1.48,-0.2,-4.67,-4.84,-2.84,-2.31,-1.95,-1.67,-1.14,-5.12,-3.71,-3.07],

'y':[0.68,-0.05,-2.41,-0.75,-1.41,-1.34,-1.99,-1.42,-2.95,-0.79,0.25,0.67,1.14,0.29,1.1,1.55,0.13,0.88,-1.12,-1.18,-0.49,-0.62,-2.04,-0.9,0.78,0.88,0.26,0.38,2.17,0.43,-0.11,-0.73,-1.47,-0.24,-1.12,-1.92,-1.49,-0.24,0.51,0.56,0.06,1.63,1.3,0.26,-0.22,-1.45,-0.52,-0.62,-2.05,-1.41,-0.65,0.55,0.64,-0.27,1.1,1.69,0.23,-0.12,-0.49,-1.81],
'z':[9.38,11.43,10.59,9.86,10.18,9.68,9.57,9.55,11.54,14.91,8.69,10.44,8.11,8.13,8.39,10.65,12.09,9.35,10.53,8.5,7.49,8.29,11.58,13.41,10.86,9.1,7.15,7.42,10.35,12.51,10.75,10.08,8.83,6.29,8.72,11.62,11.95,10.74,9.82,8.85,7.39,8.23,11.65,12.81,9.55,10.2,8.1,6.93,9.23,12.5,12.09,10.6,10.23,7.87,6.98,10.,11.31,10.77,9.79,9.87]}

ex_gyro_data = {
'x':[0.1,0.35,-0.19,0.,-0.08,-0.12,0.11,0.28,0.39,0.37,0.72,0.41,0.17,0.16,0.21,-0.15,-0.14,-0.22,-0.34,-0.16,-0.15,-0.18,-0.04,0.06,0.5,0.27,0.18,0.14,0.09,-0.33,-0.44,-0.32,-0.27,-0.23,-0.28,0.,0.36,0.54,0.21,0.15,0.31,0.13,-0.14,-0.21,-0.46,-0.2,-0.17,-0.24,-0.28,0.07,0.47,0.39,0.2,0.19,0.31,0.15,-0.18,-0.3,-0.37,-0.22],
'y':[-0.57,-0.04,0.13,0.18,0.42,0.24,0.21,0.19,0.25,0.17,0.07,0.19,-0.07,0.03,-0.,0.09,-0.29,-0.18,0.17,-0.08,0.2,0.18,0.11,-0.03,0.02,-0.22,-0.1,0.3,0.25,-0.24,-0.28,0.12,-0.09,0.14,0.32,0.09,-0.19,-0.12,-0.05,-0.1,-0.04,0.25,0.12,-0.02,-0.12,-0.06,-0.11,0.16,0.34,0.05,-0.18,-0.03,-0.17,-0.09,0.26,0.46,-0.19,-0.21,0.11,0.03],
'z':[-1.72,-0.92,-1.21,-1.49,-1.36,-1.04,-0.82,-0.44,-0.19,-0.,-0.49,-0.61,-0.32,-0.31,-0.4,-0.05,-0.18,-0.38,0.03,-0.35,-0.42,-0.05,0.15,-0.01,0.05,0.3,0.43,0.25,0.25,0.17,-0.09,0.03,-0.21,-0.19,-0.02,-0.13,-0.18,-0.05,0.12,0.33,0.18,0.21,0.36,-0.09,-0.21,-0.22,-0.3,0.03,0.03,-0.16,-0.11,0.06,0.36,0.29,0.09,0.21,0.04,-0.41,-0.16,-0.42]
}
ex_data = {
            'acc' : ex_acc_data,
           'gyro': ex_gyro_data,
           'freq': '10hz',
            'age' : '46',
            'gender': 'man',
            'weight': '92 kg',
            'location' : 'Himachal Pradesh, India',
            'temp' : '10 degree Celcius'
           }

def get_activity(data):
    hargpt_prompt=f"### Instruction: You are an expert on analyzing human activities based on IMU recordings.\n \
### Content: The IMU data is collected from a mobile phone attached to the user's body \
with a sampling rate of {data['freq']}. The IMU data is given in the IMU \
coordinate frame. The three-axis accelerations and gyroscopes are given below. \n \
Accelerations: \n \
x-axis: {str(data['acc']['x'])}, y-axis: {str(data['acc']['y'])}, z-axis: {str(data['acc']['z'])} \n \
Gyroscopes: \n \
x-axis: {str(data['gyro']['x'])}, y-axis: {str(data['gyro']['y'])}, z-axis: {str(data['gyro']['z'])} \n \
The person’s action belongs to one of the following categories: [step-on-stairs, walking, running]. \n \
Could you please tell me what action the person was doing based on the given \
information and IMU readings? Please make an analysis step by step. Please do not use code script."

    print(hargpt_prompt)
    activity = get_llm_output(hargpt_prompt)
    hargpt_prompt2=f"Given an elaborate analysis of a predicted action by a language model, go through the analysis and classify the action to the most probable among this list of action categories : : [stepping-on-stairs, walking, running]. \n \
    Only give the predicted action category and nothing else. \
    "
    activity = get_llm_output(hargpt_prompt2)
    return activity

def get_recommendation(activity, data):
    recommendation_prompt=f"### Instruction: You are a health monitoring and alert device, you give recommendation to users based on a predicted activity summary. \n \
### Content: This is a summary of the predicted activity : \"{activity}\" \n \
The user is {data['age']} years old and is of weight {data['weight']}, this user is now at {data['location']} where the current temperature is {data['temp']} \n \
Based on these information please mention if user's current activity might be unsafe for their health and in case it's unsafe recommend whether the user should take a break or slow down or change the type of activity. Be short, precise and address the user directly. Do not repeat the predicted action back.\
"
    print(recommendation_prompt)
    reco = get_llm_output(recommendation_prompt)
    return reco

# if __name__ == "__main__":
#     activity = get_activity(ex_data)
#     reco = get_recommendation(activity, ex_data)
#
#     print("Recommendation : ", reco)
