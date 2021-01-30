from alphabets import alphabets_dict


def main():
    is_process_stopped = False
    while not is_process_stopped:
        lang = input("Type your language to work with (ru, en): ").strip().lower()
        action = input("Do you want to decode or encode your message? (decode/encode) ").lower()
        user_text = input("Type anything you want: ").lower()
        shifted_value = int(input("Type value for shifting: "))
        chosen_lang = alphabets_dict[lang]
        shifted_value = preserve_oversize(shifted_value, chosen_lang)
        print(caesar_in_action(action, user_text, shifted_value, chosen_lang))
        is_continue = input('Type "n" if you want to exit the program: ').lower()
        if is_continue == "n":
            is_process_stopped = True


def caesar_in_action(action, user_text, shifted_value, chosen_lang):
    if action == "decode":
        shifted_value *= -1
    result = ''
    for char in user_text:
        if char in chosen_lang:
            shifted_index = chosen_lang.index(char) + shifted_value
            if shifted_index >= len(chosen_lang):
                result += chosen_lang[shifted_index - len(chosen_lang)]
            else:
                result += chosen_lang[shifted_index]
        else:
            result += char
    return result


def preserve_oversize(shifted_value, chosen_lang):
    # предотвращаем большое переполнение
    shifted_value = shifted_value % len(chosen_lang)
    return shifted_value


main()
