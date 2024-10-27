from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from mediapp.auth import login_required
from mediapp.db import get_db

bp = Blueprint('media', __name__)

@bp.route('/')
@login_required
def index():
    return render_template('media/index.html')

@bp.route('/movies')
@login_required
def movies():
    db = get_db()
    movies = db.execute(
        'SELECT id, title, rating, review FROM movies WHERE user_id = ?',
        (g.user['id'],)
    ).fetchall()
    return render_template('media/movies.html', movies=movies)

@bp.route('/series')
@login_required
def series():
    db = get_db()
    series = db.execute(
        'SELECT id, title, rating, review, season, episode, status, added_on'
        ' FROM series WHERE user_id = ?'
        ' ORDER BY rating DESC', (g.user['id'],)
    ).fetchall()
    return render_template('media/series.html', series=series)

@bp.route('/add_movie', methods=('GET', 'POST'))
@login_required
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        rating = request.form['rating']
        review = request.form.get('review')
        db = get_db()
        db.execute(
            'INSERT INTO movies (user_id, title, rating, review)'
            ' VALUES (?, ?, ?, ?)',
            (g.user['id'], title, rating, review)
        )
        db.commit()
        flash('The movie has been added successfully!', 'success')
        return redirect(url_for('media.movies'))

    return render_template('media/add_movie.html')

@bp.route('/add_series', methods=('GET', 'POST'))
@login_required
def add_series():
    if request.method == 'POST':
        title = request.form['title']
        rating = request.form['rating']
        review = request.form.get('review')
        episode = request.form.get('episode', 1)
        status = request.form.get('status', 'watching')
        db = get_db()
        db.execute(
            'INSERT INTO series (user_id, title, rating, review, episode, status)'
            ' VALUES (?, ?, ?, ?, ?, ?)',
            (g.user['id'], title, rating, review, episode, status)
        )
        db.commit()
        flash('The TV show has been added successfully!', 'success')
        return redirect(url_for('media.series'))

    return render_template('media/add_series.html')

@bp.route('/toggle_status/<int:id>', methods=['POST'])
@login_required
def toggle_status(id):
    db = get_db()
    serie = db.execute(
        'SELECT status FROM series WHERE id = ? AND user_id = ?',
        (id, g.user['id'])
    ).fetchone()

    # Cambia el estado a 'completado' si es 'viendo', y viceversa
    new_status = 'completed' if serie['status'] == 'watching' else 'watching'
    db.execute(
        'UPDATE series SET status = ? WHERE id = ? AND user_id = ?',
        (new_status, id, g.user['id'])
    )
    db.commit()
    return redirect(url_for('media.series'))


# Edit Movie Route
@bp.route('/edit_movie/<int:id>', methods=('GET', 'POST'))
@login_required
def edit_movie(id):
    db = get_db()
    movie = db.execute(
        'SELECT * FROM movies WHERE id = ? AND user_id = ?',
        (id, g.user['id'])
    ).fetchone()

    if request.method == 'POST':
        title = request.form['title']
        rating = request.form['rating']
        review = request.form.get('review')

        db.execute(
            'UPDATE movies SET title = ?, rating = ?, review = ? WHERE id = ? AND user_id = ?',
            (title, rating, review, id, g.user['id'])
        )
        db.commit()
        flash('The movie has been updated successfully!', 'success')
        return redirect(url_for('media.movies'))

    return render_template('media/edit_movie.html', movie=movie)


# Delete Movie Route
@bp.route('/delete_movie/<int:id>', methods=('POST',))
@login_required
def delete_movie(id):
    db = get_db()
    db.execute(
        'DELETE FROM movies WHERE id = ? AND user_id = ?',
        (id, g.user['id'])
    )
    db.commit()
    flash('The movie has been deleted successfully!', 'success')
    return redirect(url_for('media.movies'))


# Edit Series Route
@bp.route('/edit_series/<int:id>', methods=('GET', 'POST'))
@login_required
def edit_series(id):
    db = get_db()
    serie = db.execute(
        'SELECT * FROM series WHERE id = ? AND user_id = ?',
        (id, g.user['id'])
    ).fetchone()

    if request.method == 'POST':
        title = request.form['title']
        rating = request.form['rating']
        review = request.form.get('review')
        episode = request.form.get('episode', 1)
        status = request.form.get('status', 'watching')

        db.execute(
            'UPDATE series SET title = ?, rating = ?, review = ?, episode = ?, status = ? WHERE id = ? AND user_id = ?',
            (title, rating, review, episode, status, id, g.user['id'])
        )
        db.commit()
        flash('The TV show has been updated successfully!', 'success')
        return redirect(url_for('media.series'))

    return render_template('media/edit_series.html', serie=serie)


# Delete Series Route
@bp.route('/delete_series/<int:id>', methods=('POST',))
@login_required
def delete_series(id):
    db = get_db()
    db.execute(
        'DELETE FROM series WHERE id = ? AND user_id = ?',
        (id, g.user['id'])
    )
    db.commit()
    flash('The TV show has been deleted successfully!', 'success')
    return redirect(url_for('media.series'))