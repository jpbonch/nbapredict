var teamselect = document.getElementById("team");
teamselect.disabled = true;
var playertab = document.getElementById('playertab');
playertab.style.display = 'none';

var teamtabbutton = document.getElementById('teamtabbutton');
teamtabbutton.style.backgroundColor = '#363636';
var playertabbutton = document.getElementById('playertabbutton');
playertabbutton.style.color = '#363636'

var teamseveryyear = JSON.parse(teamseveryyear);

function enableteamselector() {
  var form = document.getElementById("year");
  var selected = form.options[form.selectedIndex].text;

  if (!(selected == 'noneselected')) {
    teamselect.disabled = false;
    if (selected >= 2017) {
      var teams = teamseveryyear['2017']
    }
    if (selected == 2016) {
      var teams = teamseveryyear['2016']
    }
    if (selected == 2014 || selected == 2015) {
      var teams = teamseveryyear['2014']
    }
    if (selected == 2013) {
      var teams = teamseveryyear['2013']
    }
    if (selected == 2012) {
      var teams = teamseveryyear['2012']
    }
    if (selected >= 2008 && selected <= 2011) {
      var teams = teamseveryyear['2008']
    }
    if (selected == 2007) {
      var teams = teamseveryyear['2007']
    }
    if (selected == 2005 || selected == 2006) {
      var teams = teamseveryyear['2005']
    }
    if (selected == 2003 || selected == 2004) {
      var teams = teamseveryyear['2003']
    }
    if (selected == 2002) {
      var teams = teamseveryyear['2002']
    }
    if (selected == 2001) {
      var teams = teamseveryyear['2001']
    }
    if (selected >= 1997 && selected <= 2000){
      var teams = teamseveryyear['1997']
    }
    var teamdropdown = document.getElementById('team');
    for (team of teams) {
      var teamlisting = document.createElement("option");
      teamlisting.innerHTML = team;
      teamlisting.value = team;
      teamdropdown.appendChild(teamlisting);
    }
  }
}

function clickteamtab() {
  var playertab = document.getElementById('playertab');
  playertab.style.display = 'none';
  var teamtab = document.getElementById('teamtab');
  teamtab.style.display = 'block';
  teamtabbutton.style.backgroundColor = '#363636';
  playertabbutton.style.backgroundColor = 'lightgray';
  playertabbutton.style.color = '#363636';
  teamtabbutton.style.color = 'white';
}

function clickplayertab() {
  var playertab = document.getElementById('playertab');
  playertab.style.display = 'block';
  var teamtab = document.getElementById('teamtab');
  teamtab.style.display = 'none';
  teamtabbutton.style.backgroundColor = 'lightgray';
  playertabbutton.style.backgroundColor = '#363636';
  playertabbutton.style.color = 'white';
  teamtabbutton.style.color = '#363636';
}

function onteamselected(){
  var submitbutton = document.getElementById('teamsubmit');
  submitbutton.click();
  var form = document.getElementById("team");
  var selected = form.options[form.selectedIndex].text;
}
