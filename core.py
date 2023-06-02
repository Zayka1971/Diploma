import vk_api
from config import access_token
from vk_api.exceptions import ApiError


class VkTools():
    def __init__(self, token):
        self.ext_api = vk_api.VkApi(token=access_token)

    def get_profile_info(self, user_id):

        try:
            info = self.ext_api.method('users.get',
                                       {'user_id': user_id,
                                        'fields': 'bdate,city,sex'
                                        }
                                       )
        except ApiError:
            return

        return info

    def user_serch(self, city_id, age_from, age_to, sex, offset=None):

        try:
            profiles = self.ext_api.method('users.search',
                                           {'city_id': city_id,
                                            'age_from': age_from,
                                            'age_to': age_to,
                                            'sex': sex,
                                            'count': 30,
                                            'offset': offset
                                            })

        except ApiError:
            return

        profiles = profiles['items']

        result = []
        for profile in profiles:
            if not profile['is_closed']:
                result.append({'name': profile['first_name'] + ' ' + profile['last_name'],
                               'id': profile['id']
                               })

                return result

    def photos_get(self, user_id):
        attachments = []
        photos = self.ext_api.method('photos.get',
                                     {'album_id': 'profile',
                                      'owner_id': user_id
                                      }
                                     )
        top_photo = []
        for photo in photos['items']:
            top_photo.append({'top': photo['likes']['count'], 'owner_id': photo['user_id'], 'id': photo['id']})
            top_photo = sorted(top_photo, key=lambda x: x['top'], reverse=True)
            for num in enumerate(photos):
                attachments.append({'owner_id': photo['owner_id'],
                                    'id': photo['id']
                                    })
                if num == 3:
                    break

            return attachments

        if __name__ == '__main__':
            tools = VkTools(access_token)

        print(top_photo)