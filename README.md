# WatchMate

A comprehensive Django REST API for managing movie and TV show watchlists, streaming platforms, and user reviews with ratings. Built with Django REST Framework, this application allows users to create, update, and manage their entertainment watchlists while providing a platform for community reviews and ratings.

## Features

- **Streaming Platforms Management**: CRUD operations for streaming platforms (Netflix, Hulu, etc.)
- **Watchlist Management**: Create and manage personal watchlists of movies and TV shows
- **User Reviews & Ratings**: Authenticated users can leave reviews (1-5 stars) and descriptions
- **Rating Calculations**: Automatic average rating calculation for watchlists
- **Authentication**: User registration, login, and logout with token-based authentication
- **Permissions**: Admin-only write access for platforms and watchlists, user-specific review management
- **Throttling**: Rate limiting for review creation and listing to prevent abuse
- **Filtering & Pagination**: Advanced filtering, searching, and pagination for better API performance
- **Data Validation**: Comprehensive validation for all inputs

## Tech Stack

- **Backend**: Django 6.0.3
- **API Framework**: Django REST Framework 3.17.0
- **Database**: SQLite3 (default, can be configured for PostgreSQL/MySQL)
- **Authentication**: Token-based authentication
- **Filtering**: Django Filter 25.2
- **Other**: SQLParse, ASGI, TZData

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd watchmate
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## Usage

### API Endpoints

All API endpoints are prefixed with `/watch/` unless otherwise noted.

#### Authentication Endpoints (`/account/`)

- `POST /account/register/` - User registration
- `POST /account/login/` - User login (returns auth token)
- `POST /account/logout/` - User logout

#### Watchlist Endpoints

- `GET /watch/list/` - List all watchlist items
- `POST /watch/list/` - Create new watchlist item (admin only)
- `GET /watch/<id>/` - Get specific watchlist item
- `PUT /watch/<id>/` - Update watchlist item (admin only)
- `DELETE /watch/<id>/` - Delete watchlist item (admin only)

#### Streaming Platform Endpoints

- `GET /watch/stream/` - List all streaming platforms
- `POST /watch/stream/` - Create new streaming platform (admin only)
- `GET /watch/stream/<id>/` - Get specific streaming platform
- `PUT /watch/stream/<id>/` - Update streaming platform (admin only)
- `DELETE /watch/stream/<id>/` - Delete streaming platform (admin only)

#### Review Endpoints

- `GET /watch/<watchlist_id>/reviews/` - List reviews for a watchlist
- `POST /watch/<watchlist_id>/review-create/` - Create review for watchlist (authenticated users)
- `GET /watch/review/<review_id>/` - Get specific review
- `PUT /watch/review/<review_id>/` - Update review (review owner only)
- `DELETE /watch/review/<review_id>/` - Delete review (review owner only)
- `GET /watch/reviews/?username=<username>` - Get reviews by specific user

### Authentication

1. Register a new user account via `POST /account/register/`
2. Login to get authentication token via `POST /account/login/`
3. Include the token in request headers: `Authorization: Token <your-token>`

### Example API Usage

#### Create a Streaming Platform (Admin only)
```bash
curl -X POST http://127.0.0.1:8000/watch/stream/ \
  -H "Authorization: Token <admin-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Netflix",
    "about": "Worldwide streaming service",
    "website": "https://netflix.com"
  }'
```

#### Create a Watchlist Item (Admin only)
```bash
curl -X POST http://127.0.0.1:8000/watch/list/ \
  -H "Authorization: Token <admin-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The Matrix",
    "storyline": "A computer hacker learns about the true nature of reality",
    "platform": 1,
    "active": true
  }'
```

#### Create a Review (Authenticated user)
```bash
curl -X POST http://127.0.0.1:8000/watch/1/review-create/ \
  -H "Authorization: Token <user-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "rating": 5,
    "description": "Amazing movie!"
  }'
```

## Data Models

### StreamPlatform
- `id`: Primary key
- `name`: Platform name (max 30 chars)
- `about`: Description (max 150 chars)
- `website`: Platform website URL

### Watchlist
- `id`: Primary key
- `title`: Movie/TV show title (max 255 chars)
- `storyline`: Brief description (max 200 chars)
- `active`: Boolean status
- `platform`: Foreign key to StreamPlatform
- `created`: Auto timestamp
- `avg_rating`: Calculated average rating
- `number_rating`: Count of ratings

### Review
- `id`: Primary key
- `review_user`: Foreign key to User
- `rating`: Integer 1-5 with validation
- `description`: Review text (max 200 chars, optional)
- `watchlist`: Foreign key to Watchlist
- `active`: Boolean status
- `created`: Auto timestamp
- `update`: Auto update timestamp

## Advanced Features

### Filtering
- Reviews can be filtered by `review_user__username` and `active` status
- Watchlists support ordering by `avg_rating`

### Pagination
- Configurable pagination for large result sets
- Cursor-based pagination available

### Throttling
- Review creation: Limited per user
- Review listing: Rate limited
- Scoped throttling for review details

### Permissions
- Admin users: Full CRUD on platforms and watchlists
- Authenticated users: Can create reviews, manage own reviews
- Read-only access for unauthenticated users

## Development

### Running Tests
```bash
python manage.py test
```

### Code Formatting
Ensure code follows Django best practices and PEP 8 standards.

### Database
The project uses SQLite by default. For production, configure PostgreSQL or MySQL in `settings.py`.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions or issues, please open an issue on the GitHub repository.</content>
<parameter name="filePath">c:\Users\tusha_jl2fyei\Desktop\Projects\watchmate\README.md