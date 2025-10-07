
## 🏆 Restaurant Rating Prediction

### 📌 Objective

Build a **machine learning model** to predict the **aggregate rating** of a restaurant based on other features such as location, cuisines, cost, and service availability.

---

### 📂 Project Structure

```
├── Dataset.csv
├── model.pkl
├── le_city.pkl
├── restaurant_rating_prediction.ipynb
├── README.md
```

---

### ⚙️ Steps Involved

#### 1. **Data Preprocessing**

* Loaded the dataset using `pandas`.
* Dropped irrelevant columns (e.g., IDs, location details, latitude/longitude, etc.).
* Handled **missing values** by dropping rows with nulls.
* Created a new feature:

  * `Cuisine Count` — number of cuisines a restaurant offers.
* Encoded categorical variables:

  * Binary columns (`Yes/No`) converted to 1/0.
  * `Rating text` converted to ordinal numeric scale (Not rated → 0, Excellent → 5).
  * `City` encoded using `LabelEncoder`.

#### 2. **Exploratory Data Analysis (EDA)**

* Checked for missing values and data types.
* Examined distribution of cities, ratings, and cuisines.
* Created additional derived features for better learning.

#### 3. **Model Building**

Two regression models were trained:

* **Linear Regression**
* **Decision Tree Regressor**

Each model was evaluated using:

* **Mean Squared Error (MSE)**
* **R² Score**

#### 4. **Model Evaluation**

| Model                   | R² Score         | MSE               |
| :---------------------- | :--------------- | :---------------- |
| Linear Regression       | *(your R² here)* | *(your MSE here)* |
| Decision Tree Regressor | *(your R² here)* | *(your MSE here)* |

*(Replace with your actual results after running the notebook)*

---


### 💾 Model Saving

The trained model and label encoder were saved using `pickle`:

```python
pickle.dump(dt, open('model.pkl', 'wb'))
pickle.dump(le_city, open('le_city.pkl', 'wb'))
```

These files can later be used for inference in deployment or API integration.

---


### 👨‍💻 Author

**Akshitha Chittireddy**
📧 [Gmail](mailto:akshithachittireddy1478@gmail.com)



