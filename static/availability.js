//___________blocking past days______________
document.getElementById("appointment-date").addEventListener( "focus" , function () {
  let today = new Date();
  let dd = String(today.getDate()).padStart(2, '0');
  let mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
  let yyyy = today.getFullYear();

  today = yyyy + '-' + mm + '-' + dd;
  document.getElementById("appointment-date").setAttribute("min", today);
}) ;


//_________get appointments and doctor slots ___________________
const available_slots = document.getElementById("available_slots").value;
const doctor_appointments = document.getElementById("appointments").value;

//__________convert to java array___________
const availableSlots = JSON.parse(available_slots) ;
const doctorAppointments = JSON.parse(doctor_appointments);


document.getElementById("appointment-date").addEventListener("change", function () {
  
  let selectedDate = this.value;  // selected from calender
  let slotSelect = document.getElementById("slot");
  slotSelect.innerHTML = '<option value="">Select a slot</option>';

  let today = new Date();
 

  
  let bookedSlots = doctorAppointments
    .filter(function(appointment) {          //(filter)return true if appointment with same date as selected date
      return appointment.date === selectedDate;
    })
    .map(function(appointment) {  //(map) create array with filtered appointmets
      return appointment.slot;
    });

    let filteredSlots = availableSlots.filter(function(slot) {
      if (selectedDate === today.toISOString().split('T')[0]) {
        let nowHour = today.getHours();
        let slotHour = parseInt(slot.split(":")[0], 10); 
        // Exclude slots that are before the current hour on today's date
        if (slotHour <= nowHour) {
          return false;
        }
      }
      // Exclude slots that are already booked
      return bookedSlots.indexOf(slot) === -1;
    });

  if (filteredSlots.length === 0) {
    let option = document.createElement("option");
    option.value = "";
    option.textContent = "No slots available on this day";
    slotSelect.appendChild(option);
  } else {

    filteredSlots.forEach(function(slot) {
    let option = document.createElement("option");
    option.value = slot;
    option.textContent = slot;
    slotSelect.appendChild(option);
      
    });
  }
});