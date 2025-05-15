import subprocess
import shutil
import os
import glob  # Make sure to import glob
from datetime import datetime


def compile_tex_to_pdf():
    tex_file_name = "Resume Template.tex"  # Specific LaTeX file to use
    if os.path.exists(tex_file_name):
        try:
            # Compile the LaTeX file to PDF
            subprocess.run(["pdflatex", tex_file_name], check=True)

            # Cleanup intermediate files
            for ext in ['out', 'log', 'aux']:
                try:
                    os.remove(tex_file_name[:-3] + ext)
                except FileNotFoundError:
                    print(f"{ext} file not deleted, it may not exist.")

            # Prepare directories
            old_tex_directory = "Old Tex/"
            resume_versions_directory = "Resume Versions/"
            if not os.path.exists(old_tex_directory):
                os.makedirs(old_tex_directory)
            if not os.path.exists(resume_versions_directory):
                os.makedirs(resume_versions_directory)

            # Generate timestamp for versioning
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

            # Prepare new file names with timestamp
            new_tex_name = f"{tex_file_name[:-4]}-{timestamp}.tex"
            new_pdf_name = f"{tex_file_name[:-4]}-{timestamp}.pdf"

            # Backup the original tex file with new version name
            shutil.copy(tex_file_name, os.path.join(
                old_tex_directory, new_tex_name))

            # Find the newly created PDF and move it to the resume versions directory with new version name
            pdf_files = glob.glob("*.pdf")
            if pdf_files:
                shutil.move(pdf_files[0], os.path.join(
                    resume_versions_directory, new_pdf_name))
                # Also update the main directory PDF with a consistent name
                shutil.copy(os.path.join(resume_versions_directory,
                            new_pdf_name), 'Sahand Sorouri - Senior Product Manager.pdf')

            print(
                f"Successfully compiled {tex_file_name} to PDF and backed up versions.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to compile {tex_file_name}. Error: {e}")
    else:
        print(f"No file found named {tex_file_name} in the current directory.")


# Call the function
compile_tex_to_pdf()
