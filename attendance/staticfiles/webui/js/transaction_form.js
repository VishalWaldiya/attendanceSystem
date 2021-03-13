$(document).ready(function(){
    $('#id_ID').on('change', function() {
        console.log(this.value)
        $.ajax({
            type: "GET",
            url: "/api/v1/member/" + this.value,
            dataType: "json",
            success: function (result, status, xhr) {
                console.log(result)
                $('#id_MemberType').val(result.MemberTypeDetails).prop('readonly','true');

                $('#id_name').val(result.name).prop('readonly','true');

                $('#id_CenterDetails').val(result.CenterDetails).prop('readonly','true');

                $('#id_FatherName').val(result.father_name).prop('readonly','true');

                $('#id_Gender').val(result.gender).prop('readonly','true');

                $('#id_Contact').val(result.phone_number).prop('readonly','true');
                
                $('#id_id_AlternateContact').val(result.phone_number_alt).prop('readonly','true');

                $('#id_Department').val(result.department).prop('readonly','true');

            },
            error: function (xhr, status, error) {
                alert("Result: " + status + " " + error + " " + xhr.status + " " + xhr.statusText)
            }
        });
    });

    $('form').on('submit',function(){
        var inTime = new Date($('#id_inTime').val())
        var outTime = new Date($('#id_outime').val())
        $(this).append(inTime,outTime);
        return true;
    });

});