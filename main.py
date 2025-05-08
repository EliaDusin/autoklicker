input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (Oliver == 0) {
        Oliver = 1
    } else {
        Oliver = 0
    }
})
input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    Häufigkeit += 100
    basic.showNumber(Häufigkeit)
})
input.onButtonEvent(Button.AB, input.buttonEventClick(), function () {
    Licht.set(LedSpriteProperty.X, randint(0, 4))
    Licht.set(LedSpriteProperty.Y, randint(0, 4))
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    Häufigkeit += -100
    basic.showNumber(Häufigkeit)
})
let Oliver = 0
let Licht: game.LedSprite = null
let Häufigkeit = 0
Häufigkeit = 0
Licht = game.createSprite(2, 2)
Oliver = 0
loops.everyInterval(Häufigkeit, function () {
    if (Oliver == 1) {
        Licht.set(LedSpriteProperty.X, randint(0, 4))
        Licht.set(LedSpriteProperty.Y, randint(0, 4))
    }
})
