
/**************************************/
/************   EVENT'S   *************/
/**************************************/

//General JQuery function for click of the document.
$(document).ready(function(){
    $(document).click(function(event){

        var boolNotInUserBar=false;
        var boolNotInUser=false;
        var boolNotInMainMenu=false;
        var boolNotInThreeBar=false;
        var boolNotInMainX=false;

        //Test each container to make sure we have clicked outside     
        var container = $("#idHiddenUserDiv");
        if(!container.is(event.target) && container.has(event.target).length===0 )
        {
            boolNotInUserBar=true;
        }
        container = $("#idUserLink");
        if(!container.is(event.target) && container.has(event.target).length===0 )
        {
            boolNotInUser=true;
        }
        container = $("#idMainMenuPhone");
        if(!container.is(event.target) && container.has(event.target).length===0 )
        {
            boolNotInMainMenu=true;
        }
        container = $("#idTitleThreeBars");
        if(!container.is(event.target) && container.has(event.target).length===0 )
        {
            boolNotInThreeBar=true;
        }
        container = $("#idTitleCancel");
        if(!container.is(event.target) && container.has(event.target).length===0 )
        {
            boolNotInMainX=true;
        }

        //Potentially hide the menu's
        if (boolNotInUser && boolNotInUserBar && boolNotInMainMenu && boolNotInThreeBar && boolNotInMainX)
        {
            hideMenus(true,false,true);

            //Potentially show the 3 bars or cross icon
            resetThreeBarAndX();
        }

    });
});

//JQuery function run once the document has loaded.   Used to ensure menu links are selected
$(document).ready(function() {
    //Get the path of the current window
    var pathname = window.location.pathname;
    //Scan through the links in the nav menu.
    $('#idMainMenuNOTPhone').find('a').each(function() {
        if($(this).attr('href')==pathname)
        {
            //Add selected class if it is not present
            if(!$(this).hasClass('a__MainMenuNOTPhone_selected'))
            {
                $(this).addClass('a__MainMenuNOTPhone_selected');
            }
        }
        else
        {
            //Remove selected class if it is present, but not required.
            if($(this).hasClass('a__MainMenuNOTPhone_selected'))
            {
                $(this).removeClass('a__MainMenuNOTPhone_selected');
            }
        }
    });
});

//General JQuery function for resize of window, with a delay of 500 ms
$(document).ready(function(){
    jQuery(window).resize(function() {
        delay_exec('winResize1000',500,function(){

            if(!isMobileView())
            {
                MainMenuPhone_hide();
            }

            //If we resize the window, make sure the appropriate ThreeBar/X icon is shown.
            resetThreeBarAndX();
            
        });
    });
});

// Function for delaying execution of code.   Useful to prevent multiple calls when we are
// resizing.
function delay_exec( id, wait_time, callback_f ){

    // IF WAIT TIME IS NOT ENTERED IN FUNCTION CALL,
    // SET IT TO DEFAULT VALUE: 0.5 SECOND
    if( typeof wait_time === "undefined" )
        wait_time = 500;

    // CREATE GLOBAL ARRAY(IF ITS NOT ALREADY CREATED)
    // WHERE WE STORE CURRENTLY RUNNING setTimeout() FUNCTION FOR THIS ID
    if( typeof window['delay_exec'] === "undefined" )
        window['delay_exec'] = [];

    // RESET CURRENTLY RUNNING setTimeout() FUNCTION FOR THIS ID,
    // SO IN THAT WAY WE ARE SURE THAT callback_f WILL RUN ONLY ONE TIME
    // ( ON LATEST CALL ON delay_exec FUNCTION WITH SAME ID  )
    if( typeof window['delay_exec'][id] !== "undefined" )
        clearTimeout( window['delay_exec'][id] );

    // SET NEW TIMEOUT AND EXECUTE callback_f WHEN wait_time EXPIRES,
    // BUT ONLY IF THERE ISNT ANY MORE FUTURE CALLS ( IN wait_time PERIOD )
    // TO delay_exec FUNCTION WITH SAME ID AS CURRENT ONE
    window['delay_exec'][id] = setTimeout( callback_f , wait_time );
}

/**************************************/
/************   CLICK'S   *************/
/**************************************/

//JQuery code - click the user link.
$(document).ready(function(){
    $("#idUserLink").click(function(event){
        
        //Hide all other menu's
        hideMenus(false,true,true);

        if(!UserMenu_isVisible())
        {

            //Fade In the search bar
            UserMenu_show();

        }
        else
        {
            //Fade Out the search bar
            UserMenu_hide();

        }

        //Show/Hide ThreeBar icon and X icon.
        resetThreeBarAndX();

    });
});

//JQuery code - click the top right search link.
$(document).ready(function(){
    $("#idSearchLink").click(function(event){

        //Hide all other menu's
        hideMenus(true,false,true);

        if(!SearchMenu_isVisible())
        {
            SearchMenu_show();
        }
        else
        {
            SearchMenu_hide();

            //Clear the box
            objMenu=document.getElementById("idHiddenSearchFormInput");
            objMenu.value=""

        }

        //Show/Hide ThreeBar icon and X icon.
        resetThreeBarAndX();
    });
});

//JQuery code - click the x button to close the search bar.
$(document).ready(function(){
    $("#idCloseSearch").click(function(event){

        //Hide all other menu's
        hideMenus(false,true,false);

        //Show/Hide ThreeBar icon and X icon.
        resetThreeBarAndX();

    });
});

//JQuery code - click the 3 bars icon.
$(document).ready(function(){
    $("#idTitleThreeBars").click(function(event){
        
        //Hide all other menu's
        hideMenus(true,false,false);

        if(!MainMenuPhone_isVisible())
        {
            //Fade In
            MainMenuPhone_show();

        }

        //Show/Hide ThreeBar icon and X icon.
        resetThreeBarAndX();
    });
});

//JQuery code - click the x icon.
$(document).ready(function(){
    $("#idTitleCancel").click(function(event){
        
        //Hide menu's
        hideMenus(false,false,true);

        //Hide the x and show the 3 bars
        resetThreeBarAndX();

    });
});

/**************************************/
/***   CALLED JAVASCRIPT FUNCTIONS   **/
/**************************************/



/**************************************/
/********   ACTION FUNCTIONS   ********/
/**************************************/

//Called by JQuery functions after menu's have been shown/hidden.   It ensures that the ThreeBar icon and
//X icon displayed are consistent with the menu's that are visible.
function resetThreeBarAndX()
{
    //ensure the appropriate 3bar/cross icon is visible
    if(isMobileView())
    {
        if(MainMenuPhone_isVisible())
        {
            CrossIcon_show();
            ThreeBarIcon_hide();
        }
        else
        {
            CrossIcon_hide();
            ThreeBarIcon_show();
        }
    }
    else
    {
        CrossIcon_hide();
        ThreeBarIcon_hide();
    }
};

//Called by JQuery functions to hide the user dropdown and/or search dropdown.
function hideMenus(boolUser, boolSearch, boolTitle)
{
    if(UserMenu_isVisible() && boolUser)
    {
        UserMenu_hide();
    }
    if(SearchMenu_isVisible() && boolSearch)
    {
        SearchMenu_hide();
    }
    if(MainMenuPhone_isVisible() && boolTitle)
    {
        MainMenuPhone_hide();
    }
};

function SearchMenu_hide()
{
    $("#idHiddenSearchForm").hide();
};
function SearchMenu_show()
{
    $("#idHiddenSearchForm").fadeIn();
};

function UserMenu_hide()
{
    $("#idHiddenUserDiv").hide();
};
function UserMenu_show()
{
    $("#idHiddenUserDiv").fadeIn();
};

function MainMenuPhone_hide()
{
    $("#idMainMenuPhone").hide();
};
function MainMenuPhone_show()
{
    $("#idMainMenuPhone").fadeIn();
};

function CrossIcon_hide()
{
    $("#idTitleCancel").hide();
};
function CrossIcon_show()
{
    $("#idTitleCancel").fadeIn();
};
function ThreeBarIcon_hide()
{
    $("#idTitleThreeBars").hide();
};
function ThreeBarIcon_show()
{
    $("#idTitleThreeBars").fadeIn();
};
/**************************************/
/*********   TEST FUNCTIONS   *********/
/**************************************/

function UserMenu_isVisible()
{
    return $('#idHiddenUserDiv').is(':visible');
};

function SearchMenu_isVisible()
{
    return $('#idHiddenSearchForm').is(':visible');
};

function MainMenuPhone_isVisible()
{
    return $('#idMainMenuPhone').is(':visible');
};

function isMobileView()
{
    var x = window.matchMedia("(max-width: 600px)");
    return x.matches
};