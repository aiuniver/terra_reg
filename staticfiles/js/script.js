"use strict";


(($) => {


    $(() => {

        $("input[type=text],input[type=email]").bind("focus", (event) => {
            $(event.currentTarget).closest(".form-group").addClass("focused");
        }).bind("blur", (event) => {
            let item = $(event.currentTarget),
                field = item.closest(".form-group");
            if (item.val() !== "") field.addClass("focused");
            else field.removeClass("focused");
        }).each((index, item) => {
            let field = $(item).closest(".form-group");
            if (item.value !== "") field.addClass("focused");
            else field.removeClass("focused");
        });

    });


})(jQuery);
