# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from PIL import Image
# from collections import Counter
# import os
# import bcrypt
# import mysql.connector as connector
# from werkzeug.utils import secure_filename
# from ultralytics import YOLO
# from dotenv import load_dotenv

# # --- Local Imports ---
# # Import centralized data and the updated video processor function
# import config
# from video_processor import process_video_for_repair_estimate

# # --- Environment Setup ---
# dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
# load_dotenv(dotenv_path)

# app = Flask(__name__)
# app.secret_key = "FDMYD-9NK6Q-FHT6T-86XJ4-VMH8Y"

# # --- Paths ---
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# MODELS_DIR = os.path.join(BASE_DIR, "models")
# STATIC_DIR = os.path.join(BASE_DIR, "static")
# UPLOAD_IMAGE = os.path.join(STATIC_DIR, "uploaded_image.jpg")
# DETECTED_IMAGE = os.path.join(STATIC_DIR, "detected_image.jpg")

# os.makedirs(STATIC_DIR, exist_ok=True)

# # --- DB Connection ---
# def connect_to_db():
#     try:
#         connection = connector.connect(**config.mysql_credentials)
#         return connection
#     except connector.Error as e:
#         print(f"Database connection error: {e}")
#         return None

# # --- Routes (signup, login, etc. remain the same) ---
# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     # ... (your signup code remains unchanged)
#     if request.method == 'POST':
#         name = request.form.get('name')
#         password = request.form.get('password')
#         email = request.form.get('email')
#         vehicle_id = request.form.get('vehicleId')
#         contact_number = request.form.get('phoneNumber')
#         address = request.form.get('address')
#         car_brand = request.form.get('carBrand')
#         model_name = request.form.get('carModel')

#         if not all([name, password, email, vehicle_id, contact_number, address, car_brand, model_name]):
#             flash("All fields are required!", "error")
#             return render_template('signup.html')

#         hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
#         connection = connect_to_db()
#         if connection:
#             try:
#                 with connection.cursor() as cursor:
#                     query = """
#                     INSERT INTO user_info (name, password, email, vehicle_id, contact_number, address, car_brand, model)
#                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#                     """
#                     cursor.execute(query, (name, hashed_password, email, vehicle_id, contact_number, address, car_brand, model_name))
#                     connection.commit()
#                 session['user_email'] = email
#                 flash("Signup successful!", "success")
#                 return redirect(url_for('dashboard'))
#             except connector.IntegrityError as e:
#                 if 'Duplicate entry' in str(e):
#                     flash("Email already exists. Please use a different email.", "error")
#                 else:
#                     flash("Error during signup. Please try again.", "error")
#             except connector.Error as e:
#                 print(f"Query error: {e}")
#                 flash("Error during signup. Please try again.", "error")
#             finally:
#                 connection.close()
#         else:
#             flash("Database connection failed.", "error")
#     return render_template('signup.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # ... (your login code remains unchanged)
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')

#         if not email or not password:
#             flash("Email and password are required!", "error")
#             return render_template('login.html')

#         connection = connect_to_db()
#         if connection:
#             try:
#                 with connection.cursor() as cursor:
#                     cursor.execute("SELECT password FROM user_info WHERE email = %s", (email,))
#                     result = cursor.fetchone()
#                     if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
#                         session['user_email'] = email
#                         flash("Login successful!", "success")
#                         return redirect(url_for('dashboard'))
#                     else:
#                         flash("Invalid email or password.", "error")
#             except connector.Error as e:
#                 print(f"Query error: {e}")
#                 flash("Login error. Try again.", "error")
#             finally:
#                 connection.close()
#         else:
#             flash("Database connection failed.", "error")
#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     session.pop('user_email', None)
#     flash("Logged out successfully.", "info")
#     return redirect(url_for('login'))

# # --- YOLO Model ---
# model_path = os.path.join(MODELS_DIR, "best.pt")
# model = YOLO(model_path)

# # --- Dashboard ---
# @app.route('/dashboard', methods=['GET', 'POST'])
# def dashboard():
#     if 'user_email' not in session:
#         flash('Login required to access dashboard.', 'error')
#         return redirect(url_for('login'))

#     if request.method == 'POST':
#         file = request.files.get('file')
#         if not file or file.filename == '':
#             flash('Please upload a file.', 'error')
#             return render_template('dashboard.html')

#         filename = secure_filename(file.filename)
#         file_ext = os.path.splitext(filename)[1].lower()

#         # --- IMAGE PROCESSING ---
#         if file_ext in ['.png', '.jpg', '.jpeg']:
#             file.save(UPLOAD_IMAGE)
#             result = model(UPLOAD_IMAGE)
#             res_plotted = result[0].plot()
#             pil_img = Image.fromarray(res_plotted)
#             pil_img.save(DETECTED_IMAGE)

#             class_ids = [box.cls.item() for box in result[0].boxes]
#             class_counts = Counter(class_ids)
            
#             part_prices = get_part_prices(session['user_email'], class_counts)

#             return render_template('estimate.html',
#                                    original_image='uploaded_image.jpg',
#                                    detected_image='detected_image.jpg',
#                                    part_prices=part_prices)

#         # --- VIDEO PROCESSING ---
#         elif file_ext in ['.mp4', '.mov', '.avi', '.mkv']:
#             upload_folder = os.path.join(STATIC_DIR, 'uploads')
#             os.makedirs(upload_folder, exist_ok=True)
#             video_path = os.path.join(upload_folder, filename)
#             file.save(video_path)

#             user_car_details = get_user_car_details(session['user_email'])
#             if not user_car_details:
#                 flash('Could not retrieve your car details.', 'error')
#                 return redirect(url_for('dashboard'))

#             # The function now returns two values: prices and image paths
#             part_prices, detected_images = process_video_for_repair_estimate(video_path, model, user_car_details)

#             if not part_prices:
#                 flash('No damage was detected in the video.', 'info')
#                 return redirect(url_for('dashboard'))

#             # Pass the data to the template using the SAME variable names as the image route
#             return render_template('estimate.html',
#                                    part_prices=part_prices,
#                                    video_frames=detected_images) # Pass detected frames as a separate variable

#         else:
#             flash('Invalid file type. Please upload an image or video.', 'error')
#             return render_template('dashboard.html')

#     return render_template('dashboard.html')

# # --- Helper Functions ---
# def get_user_car_details(email):
#     connection = connect_to_db()
#     if not connection:
#         return None
#     try:
#         with connection.cursor(dictionary=True) as cursor:
#             cursor.execute("SELECT car_brand, model FROM user_info WHERE email = %s", (email,))
#             return cursor.fetchone()
#     except connector.Error as e:
#         print(f"DB error fetching user car: {e}")
#         return None
#     finally:
#         if connection.is_connected():
#             connection.close()

# def get_part_prices(email, class_counts):
#     user_car = get_user_car_details(email)
#     if not user_car:
#         return {}

#     car_brand = user_car['car_brand'].strip().upper()
#     car_model = user_car['model'].strip().title()
    
#     prices = {}
#     for class_id, count in class_counts.items():
#         # Use the centralized helper function from config
#         part_name = config.get_part_name_from_id(class_id)
#         if part_name:
#             try:
#                 # Use the centralized data from config
#                 price_per_part = config.CAR_PRICES_DATA[car_brand][car_model][part_name]
#                 total_price = price_per_part * count
#                 prices[part_name] = {
#                     'count': count,
#                     'price': price_per_part,
#                     'total': total_price
#                 }
#             except KeyError:
#                 print(f"Price not found for: {car_brand}, {car_model}, {part_name}")
#                 continue
#     return prices

# # ---
# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for, session, flash
from PIL import Image
from collections import Counter
import os
import bcrypt
import mysql.connector as connector
from werkzeug.utils import secure_filename
from ultralytics import YOLO
from dotenv import load_dotenv

# --- Local Imports ---
# Import centralized data and the updated video processor function
import config
from video_processor import process_video_for_repair_estimate

# --- Environment Setup ---
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

app = Flask(__name__)
app.secret_key = "FDMYD-9NK6Q-FHT6T-86XJ4-VMH8Y"

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")
STATIC_DIR = os.path.join(BASE_DIR, "static")
UPLOAD_IMAGE = os.path.join(STATIC_DIR, "uploaded_image.jpg")
DETECTED_IMAGE = os.path.join(STATIC_DIR, "detected_image.jpg")

os.makedirs(STATIC_DIR, exist_ok=True)

# --- DB Connection ---
def connect_to_db():
    try:
        connection = connector.connect(**config.mysql_credentials)
        return connection
    except connector.Error as e:
        print(f"Database connection error: {e}")
        return None

# --- Routes (signup, login, etc. remain the same) ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # ... (your signup code remains unchanged)
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        vehicle_id = request.form.get('vehicleId')
        contact_number = request.form.get('phoneNumber')
        address = request.form.get('address')
        car_brand = request.form.get('carBrand')
        model_name = request.form.get('carModel')

        if not all([name, password, email, vehicle_id, contact_number, address, car_brand, model_name]):
            flash("All fields are required!", "error")
            return render_template('signup.html')

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        connection = connect_to_db()
        if connection:
            try:
                with connection.cursor() as cursor:
                    query = """
                    INSERT INTO user_info (name, password, email, vehicle_id, contact_number, address, car_brand, model)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(query, (name, hashed_password, email, vehicle_id, contact_number, address, car_brand, model_name))
                    connection.commit()
                session['user_email'] = email
                flash("Signup successful!", "success")
                return redirect(url_for('dashboard'))
            except connector.IntegrityError as e:
                if 'Duplicate entry' in str(e):
                    flash("Email already exists. Please use a different email.", "error")
                else:
                    flash("Error during signup. Please try again.", "error")
            except connector.Error as e:
                print(f"Query error: {e}")
                flash("Error during signup. Please try again.", "error")
            finally:
                connection.close()
        else:
            flash("Database connection failed.", "error")
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # ... (your login code remains unchanged)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash("Email and password are required!", "error")
            return render_template('login.html')

        connection = connect_to_db()
        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT password FROM user_info WHERE email = %s", (email,))
                    result = cursor.fetchone()
                    if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
                        session['user_email'] = email
                        flash("Login successful!", "success")
                        return redirect(url_for('dashboard'))
                    else:
                        flash("Invalid email or password.", "error")
            except connector.Error as e:
                print(f"Query error: {e}")
                flash("Login error. Try again.", "error")
            finally:
                connection.close()
        else:
            flash("Database connection failed.", "error")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_email', None)
    flash("Logged out successfully.", "info")
    return redirect(url_for('login'))

# --- YOLO Model ---
model_path = os.path.join(MODELS_DIR, "best.pt")
model = YOLO(model_path)

# --- Dashboard ---
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_email' not in session:
        flash('Login required to access dashboard.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        file = request.files.get('file')
        if not file or file.filename == '':
            flash('Please upload a file.', 'error')
            return render_template('dashboard.html')

        filename = secure_filename(file.filename)
        file_ext = os.path.splitext(filename)[1].lower()

        # --- IMAGE PROCESSING ---
        if file_ext in ['.png', '.jpg', '.jpeg']:
            file.save(UPLOAD_IMAGE)
            result = model(UPLOAD_IMAGE)
            res_plotted = result[0].plot()
            pil_img = Image.fromarray(res_plotted)
            pil_img.save(DETECTED_IMAGE)

            # Extract the necessary data: class ID and confidence score for each detection
            detections = []
            if result[0].boxes.cls.numel() > 0: # Check if any detections exist
                for box in result[0].boxes:
                    detections.append({
                        'class_id': box.cls.item(),
                        'conf': box.conf.item()
                    })
            
            # Pass the list of detections to the updated get_part_prices function
            part_prices = get_part_prices(session['user_email'], detections)

            if not part_prices:
                 flash('No damage was detected in the image.', 'info')
                 return redirect(url_for('dashboard'))

            return render_template('estimate.html',
                                   original_image='uploaded_image.jpg',
                                   detected_image='detected_image.jpg',
                                   part_prices=part_prices)

        # --- VIDEO PROCESSING ---
        elif file_ext in ['.mp4', '.mov', '.avi', '.mkv']:
            upload_folder = os.path.join(STATIC_DIR, 'uploads')
            os.makedirs(upload_folder, exist_ok=True)
            video_path = os.path.join(upload_folder, filename)
            file.save(video_path)

            user_car_details = get_user_car_details(session['user_email'])
            if not user_car_details:
                flash('Could not retrieve your car details.', 'error')
                return redirect(url_for('dashboard'))

            # The function now returns two values: prices and image paths
            # NOTE: process_video_for_repair_estimate also needs to be updated to return 
            # the prices dictionary in the same format as get_part_prices.
            part_prices, detected_images = process_video_for_repair_estimate(video_path, model, user_car_details)

            if not part_prices:
                flash('No damage was detected in the video.', 'info')
                return redirect(url_for('dashboard'))

            # Pass the data to the template using the SAME variable names as the image route
            return render_template('estimate.html',
                                   part_prices=part_prices,
                                   video_frames=detected_images) # Pass detected frames as a separate variable

        else:
            flash('Invalid file type. Please upload an image or video.', 'error')
            return render_template('dashboard.html')

    return render_template('dashboard.html')

# --- Helper Functions ---
def get_user_car_details(email):
    connection = connect_to_db()
    if not connection:
        return None
    try:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT car_brand, model FROM user_info WHERE email = %s", (email,))
            return cursor.fetchone()
    except connector.Error as e:
        print(f"DB error fetching user car: {e}")
        return None
    finally:
        if connection.is_connected():
            connection.close()

def get_part_prices(email, detections):
    """
    Calculates repair prices based on part, car model, and damage confidence score.
    
    :param email: User email to fetch car details.
    :param detections: A list of dictionaries, where each dict has 'class_id' and 'conf' (confidence score).
    :returns: A dictionary with calculated repair costs.
    """
    user_car = get_user_car_details(email)
    if not user_car:
        return {}

    car_brand = user_car['car_brand'].strip().upper()
    car_model = user_car['model'].strip().title()
    
    # Store aggregated price info for unique parts
    prices_info = {}
    CRITICAL_PARTS = ['light', 'windshield'] # List of parts that always require full replacement

    for detection in detections:
        class_id = detection['class_id']
        conf_score = detection['conf']
        
        # Use the centralized helper function from config
        part_name = config.get_part_name_from_id(class_id)
        
        if not part_name:
            continue

        try:
            # Get the base price for the part
            base_price = config.CAR_PRICES_DATA[car_brand][car_model][part_name]
        except KeyError:
            print(f"Price not found for: {car_brand}, {car_model}, {part_name}")
            continue

        # --- Apply Damage Probability Logic ---
        
        # Critical parts always take full price
        if part_name.lower() in CRITICAL_PARTS:
            cost_multiplier = 1.0 
        else:
            # Non-critical parts use confidence score (damage probability) logic
            if conf_score >= 0.7:
                cost_multiplier = 1.0    # Full price
            elif conf_score >= 0.6:
                cost_multiplier = 0.75   # 75% of price
            elif conf_score >= 0.5:
                cost_multiplier = 0.60   # 60% of price
            elif conf_score >= 0.4:
                cost_multiplier = 0.50   # 50% of price
            else:
                # Ignore very low confidence detections
                continue 

        # Calculate the repair cost for this specific detection
        repair_cost = base_price * cost_multiplier

        # Aggregate the costs and counts for the same part
        if part_name not in prices_info:
            prices_info[part_name] = {
                'count': 1,
                'price': base_price, # Store the base price for display
                'total': repair_cost, # Start with the first calculated repair cost
                'multiplier': cost_multiplier # Store the multiplier applied
            }
        else:
            prices_info[part_name]['count'] += 1
            prices_info[part_name]['total'] += repair_cost
            
    # Format the output dictionary to match the previous structure
    final_prices = {}
    for part, data in prices_info.items():
        final_prices[part] = {
            'count': data['count'],
            'price': data['price'], # Base price
            'total': data['total'], # Aggregated, calculated repair cost
            'description': f"Repair Cost based on detection confidence: {data.get('multiplier', 1.0) * 100:.0f}% of base price applied."
        }
    
    return final_prices

# ---
if __name__ == '__main__':
    app.run(debug=True)