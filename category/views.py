from django.shortcuts import render, get_object_or_404, redirect
from .models import Category,Subject
from .forms import CategoryForm,ExcelImportForm
import pandas as pd
from django.contrib import messages
# Category views
def category_list(request):
    categories = Category.objects.all()
    if request.method=="POST":
        form = ExcelImportForm(request.POST , request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['excel_file']
            try:
                df = pd.read_excel(uploaded_file)
                for index,row in df.iterrows():
                    category_id=row.get('category_id')
                    category_name=row.get('category_name')
                    subject=row.get('subject')
                    if Category.objects.filter(category_id=category_id).exists():
                        messages.warning(request,f"Category ID'{category_id}' already exist.Skipping.")
                        continue

                    Category.object.create(category_id=category_id,
                                           category_name=category_name,
                                           subject=subject)
                
                messages.success(request,"Categories imported successfully!")
            except Exception as e:
                messages.error(request, f"An error occurred during import: {e}")
            return redirect('category:category_list')
    else:
        form = ExcelImportForm()
    return render(request, 'category_list.html', {'categories': categories, 'form': form})
    
def insert_category(category_id, category_name,subject):
    try:
        Category.objects.create(
            category_id=category_id,
            category_name=category_name,
            subject=subject
        )
        return True, None
    except Exception as e:
        return False, str(e)


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})

def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category:category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category:category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})



from django.db.models import Q
from django.http import HttpResponse
import openpyxl
#--------------------------------
def import_category(request):
    if request.method == 'POST':
        form = ExcelImportForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['excel_file']
            try:
                df = pd.read_excel(uploaded_file)
                categories_imported = 0  # Đếm số lượng Category được import

                print("DataFrame contents:")
                print(df)  # Debugging

                for index, row in df.iterrows():
                    category_name = row.get("category_name")
                    subject_name = row.get("subject")
                    print(f"subject tên là {subject_name}")
                    print(f"Processing row: {category_name} and {subject_name}")  # Debugging

                    # Kiểm tra xem subject có tồn tại không
                    try:
                        subject = Subject.objects.get(name=subject_name)
                        print(f"Subject found: {subject}")  # Debugging

                        # Kiểm tra xem category_name đã tồn tại với subject đó chưa
                        if not Category.objects.filter(category_name=category_name, subject=subject).exists():
                            # Nếu không tồn tại, tạo mới Category
                            Category.objects.create(
                                category_name=category_name,
                                subject=subject
                            )
                            categories_imported += 1
                            print(f"Category '{category_name}' created with Subject '{subject}'")  # Debugging
                        else:
                            print(f"Category '{category_name}' already exists with Subject '{subject}'. Skipping.")  # Debugging

                    except Subject.DoesNotExist:
                        messages.warning(request, f"Subject '{subject_name}' does not exist. Skipping this row.")
                        print(f"Subject '{subject_name}' not found. Skipping row.")  # Debugging

                # Thông báo kết quả import
                if categories_imported > 0:
                    messages.success(request, f"{categories_imported} categories imported successfully!")
                else:
                    messages.warning(request, "No categories were imported.")

            except Exception as e:
                messages.error(request, f"An error occurred during import: {e}")
                print(f"Error during import: {e}")  # Debugging

            return redirect('category:category_list')
    else:
        form = ExcelImportForm()

    return render(request, 'category_list.html', {'form': form})







def export_category(request):
    # Create a workbook and add a worksheet
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Categories.xlsx'
    
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = 'CATEGORIES'
    
    # Define the columns
    columns = ['CATEGORY ID', 'CATEGORY Name','SUBJECT']  # Cột cho ID và Tên vai trò
    worksheet.append(columns)
    
    # Fetch all roles and write to the Excel file
    for category in Category.objects.all():
        worksheet.append([category.id, category.category_name,category.subject.name])  # Xuất ID và Tên vai trò
    
    workbook.save(response)
    return response

