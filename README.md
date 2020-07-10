# StFX-Timetable
Program to create a ics calendar based on course numbers (StFX only)

#### Required libraries
<ul>
  <li> pandas
  <li> datetmie
</ul>

#### StFX full course calendar
  https://app.stfx.ca/web/openreports/Default.aspx?procedure=PKG_COURSEINFO.Registrar_website_Timetable&parameter.p_subj=%&SUBMIT=Fetch
  
#### StFX course timeblocks
  https://www2.mystfx.ca/sites/mystfx.ca.registrars-office/files/Final_202110%20Adjusted%20Grid%20-%20Updated.pdf
  
#### How to use
  Download the files and run makeSchedule.py
  Enter CRN of each course you want to add to calendar
  Enter -1 when done
  Upload the myCourses.ics file that was created to your Google/Apple/Outlook calendar
  
#### Known issues
  Can't delete courses from ics. Have to delete the ics file and start over
  Google calendar automatically sets notifications to 30 minutes before for every entry added
  
