
/* -----------------dashboard page scripts--------------------*/


 function findlanguageid(language) {
        document.getElementById('languageid').value = language;
        var createuniquecellid='#languagetabelcell'+ language;
        var languagename = $(createuniquecellid).data('value');
        document.getElementById('languagename').value = languagename;
        $(".dashboardtablesdiv").hide();
        $(".dashboardformsdiv").hide();
        $("#languageupdateform").show();
    }


 function findcontrolid(control) {
        document.getElementById('controlid').value = control;
        var createuniquecellid='#controltabelcell'+ control;
        var controlname = $(createuniquecellid).data('value');
        document.getElementById('controlname').value = controlname;
        $(".dashboardtablesdiv").hide();
        $(".dashboardformsdiv").hide();
        $("#controlupdateform").show();
    }


 function findsyntaxid(syntax) {
        document.getElementById('syntaxid').value = syntax;
        var createlanguageuniquecellid='#syntaxlanguagetabelcell'+ syntax;
        var createcontroluniquecellid='#syntaxcontroltabelcell'+ syntax;
        var createsyntaxuniquecellid='#syntaxtabelcell'+ syntax;
        var languagename = $(createlanguageuniquecellid).data('value');
        var controlname = $(createcontroluniquecellid).data('value');
        var syntaxname = $(createsyntaxuniquecellid).data('value');
        document.getElementById('syntaxlanguageid').value = languagename;
        document.getElementById('syntaxlanguageid').innerText = languagename;
        document.getElementById('syntaxcontrolid').value = controlname;
        document.getElementById('syntaxcontrolid').innerText = controlname;
        document.getElementById('syntaxsyntax').value = syntaxname;
        $(".dashboardtablesdiv").hide();
        $("#syntaxupdateform").show();
    }


$(document).ready(function() {
      $(".sidenavlink").click(function() {
      $(".dashboardtablesdiv").hide();
      $(".dashboardformsdiv").hide();
      $("#languageupdateform").hide();
      $("#controlupdateform").hide();
      $("#syntaxupdateform").hide();
      $(".image").hide();

        var tableId = $(this).data("table");
        $(tableId).show();
      });
    });



 $(document).ready(function() {
      $(".tablebuttons").click(function() {
      $(".dashboardtablesdiv").hide();
      $(".dashboardformsdiv").hide();
      $("#languageupdateform").hide();
      $("#controlupdateform").hide();
      $("#syntaxupdateform").hide();
      $(".image").hide();

        var formId = $(this).data("form");
        $(formId).show();
      });
    });



 /*---------------------single convert page scripts--------------------*/

function selectLanguage(language) {
    document.getElementById('selectedLanguage').innerText = language;
    document.getElementById('selectedLanguageInput').value = language;
  }


function selectcontrol(control) {
    document.getElementById('selectedcontrol').innerText = control;
    document.getElementById('selectedcontrolInput').value = control;
  }


$(document).ready(function () {

        $("#convertForm").submit(function (event) {

            event.preventDefault();

            $.ajax({
                type: "POST",
                url: "/",
                data: {
                          languagename: $('#selectedLanguageInput').val(),
                          controlname: $('#selectedcontrolInput').val()

                 },

                dataType: 'text',
                success: function (data) {
                    $("#result").text(data);
                }
            });
        });
    });


/*---------------------multi convert page scripts--------------------*/


    function firstselectLanguageoptions(language) {
        document.getElementById('firstselectedLanguage').innerText = language;
        document.getElementById('firstselectedLanguageInput').value = language;
     }


     function selectcontrol(control) {
        document.getElementById('selectedcontrol').innerText = control;
        document.getElementById('selectedcontrolInput').value = control;
     }


     function secondselectLanguageoptions(language) {
        document.getElementById('secondselectedLanguage').innerText = language;
        document.getElementById('secondselectedLanguageInput').value = language;
     }



    $(document).ready(function () {

        $("#convertForm").submit(function (event) {

            event.preventDefault();

            $.ajax({
                type: "POST",
                url: "/multiconvert",
                data: {
                          firstlanguagename: $('#firstselectedLanguageInput').val(),
                          controlname: $('#selectedcontrolInput').val(),
                          secondlanguagename: $('#secondselectedLanguageInput').val()

                 },

                dataType: 'json',
                success: function (data) {
                    $("#result1").text(data.firstsyntaxresult);
                    $("#result2").text(data.secondsyntaxresult);

                }
            });
        });
    });