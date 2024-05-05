class KalmanFilter
{
public:
    KalmanFilter(float initial_state, float initial_covariance, float process_noise, float measurement_noise)
    {
        state = initial_state;
        covariance = initial_covariance;
        Q = process_noise;
        R = measurement_noise;
    }

    float predict()
    {
        // Prediction step: Project the state forward
        // Here, we assume no control input, so we omit the control matrix
        state = state; // In a more complex model, you can add motion models here
        covariance += Q;

        return state;
    }

    float update(float measurement)
    {
        // Update step: Correct the predicted state using the measurement
        float kalman_gain = covariance / (covariance + R);
        state += kalman_gain * (measurement - state);
        covariance *= (1 - kalman_gain);

        return state;
    }

    float getState()
    {
        return state;
    }

private:
    float state;
    float covariance;
    float Q; // Process noise covariance
    float R; // Measurement noise covariance
};

float initial_state = 0;
float initial_covariance = 1;
float process_noise = 0.1;
float measurement_noise = 2.0;

KalmanFilter ultrasonic1(initial_state, initial_covariance, process_noise, measurement_noise);
KalmanFilter ultrasonic2(initial_state, initial_covariance, process_noise, measurement_noise);


float *kalmanFilter(long unsigned int sensor_reading[])
{

    ultrasonic1.predict();
    ultrasonic2.predict();

    static float data[2] = {
        ultrasonic1.update(sensor_reading[0]),
        ultrasonic2.update(sensor_reading[1])
    };

    return data;
}